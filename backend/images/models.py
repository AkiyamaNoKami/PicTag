from django.conf import settings
from django.db import models
from hashlib import md5


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    hash = models.CharField(max_length=200, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="images", blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='uploaded_images', null=True, blank=True, on_delete=models.SET_NULL)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image #{self.id}'

    def fill_metadata(self):
        self.width=self.image.width
        self.height=self.image.height
        self.hash=md5(self.image.read()).hexdigest()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name