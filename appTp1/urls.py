from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<name>', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('products/list', views.ProductListView.as_view(), name='products'),
    path('product/<pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('items/list', views.ProductItemListView.as_view(), name='items'),
    path('item/<pk>', views.ProductItemDetailView.as_view(), name='item-detail'),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
]
