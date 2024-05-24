from django.db import models


class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
