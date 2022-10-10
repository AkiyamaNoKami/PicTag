from django.contrib import admin
from .models import Image, Tag
from admin_decorators import allow_tags


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'count']

    def count(self, obj):
        return obj.images.count()

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['__str__', '_preview', 'hash', 'width', 'height', '_tags']
    list_filter = ['tags']
    filter_horizontal = ['tags']

    def get_readonly_fields(self, request, obj):
        readonly_fields=['hash', 'width', 'height']
        if obj:
            readonly_fields.append('image')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.fill_metadata()
        return super().save_model(request, obj, form, change)

    @allow_tags
    def _preview(self,obj):
        return f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" height="100"></a>'

    @allow_tags
    def _tags(self, obj):
        return '<br>'.join(f'<a href="?tags__id__exact={tag.id}">{tag.name}</a>' for tag in obj.tags.all())