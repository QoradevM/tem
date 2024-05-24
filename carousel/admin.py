from django.contrib import admin
from .models import CarouselItem

class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

admin.site.register(CarouselItem, CarouselItemAdmin)
