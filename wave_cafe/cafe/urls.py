from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [

    path('about/', views.about,
      name='about'),
    path('special/', views.special,
      name='special'),
    path('contact/', views.contact,
      name='contact'),
    path('menu/', views.menu,
      name='menu'),
    path('', views.product_list, name='product_list'),

    path('<slug:category_slug>/', views.menu,
      name='product_list_by_category'),
]

