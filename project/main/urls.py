from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('brand/<int:brand_id>/', views.cars_by_brand, name='cars_by_brand'),
]