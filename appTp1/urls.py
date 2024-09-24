from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('hello/<name>', views.hello, name='hello'),
    # path('products/', views.ListProducts, name='products'),
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<name>', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('products/list', views.ProductListView.as_view(), name='products'),
    path('product/<id>', views.ProductDetailView.as_view(), name='product'),
    path('items/<id>', views.ListItemsProduct, name='items'),
]
