from operator import attrgetter

from django.http import JsonResponse
from django.views.generic import ListView, View
from django.db.models import Count

from .models import Image, Tag

class ImageListView(ListView):
    model = Image
    context_object_name = 'images'

    def get_queryset(self):
        qs = super().get_queryset()

        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(tags__name__in=q.split()).distinct()

        return qs

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if context['images']:
            tags_qs = Tag.objects.annotate(count=Count('images', distinct=True))
            tags_qs = tags_qs.filter(images__id__in=map(attrgetter('id'), context['images']))
            context['tags'] = tags_qs.order_by('name').distinct()
        context['q'] = self.request.GET.get('q')
        return context


class TagAutocompleteView(View):
    def get(self, request):
        qs = Tag.objects.all().order_by('name')

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        else:
            qs = qs.none()

        data = [{'name': tag.name} for tag in qs]

        return JsonResponse(data, safe=False)