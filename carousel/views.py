from django.shortcuts import render
from .models import CarouselItem


def home_view(request):
    carousel_items = CarouselItem.objects.all()
    return render(request, 'main.html', {'carousel_items': carousel_items})
