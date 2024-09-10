from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('hello/<name>', views.hello, name='hello'),
    path('products/', views.ListProducts, name='products'),
    path('items/<id>', views.ListItemsProduct, name='items'),
]
