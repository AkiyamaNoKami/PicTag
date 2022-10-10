from django.urls import path
from .views import ImageListView, TagAutocompleteView, ImageDetailView, ImageUploadView


app_name='images'

urlpatterns = [
    path('', ImageListView.as_view(), name='image_list'),
    path('autocomplete/tags/', TagAutocompleteView.as_view(), name='tag-autocomplete'),
    path('<int:pk>', ImageDetailView.as_view(), name='image-detail'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
]