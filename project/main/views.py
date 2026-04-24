from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    context = {
        'brands': brands,
        'cars': cars,
    }
    return render(request, 'main/index.html', context)


def car_detail(request, car_id):
    brands = Brand.objects.all()
    context = {
        'car': Car,
        'brands': brands,
    }
    return render(request, 'main/detail.html', context)


def cars_by_brand(request, brand_id):
    brands = Brand.objects.all()
    cars = Car.objects.filter(brand=brands)

    context = {
        'brands': brands,
        'cars': cars,
    }
    return render(request, 'main/index.html', context)