from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='images', null=True, max_length=255)

    def __str__(self):
        return self.title
