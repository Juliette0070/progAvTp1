from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<name>', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('product/list', views.ProductListView.as_view(), name='products'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('item/list', views.ProductItemListView.as_view(), name='items'),
    path('item/<pk>/', views.ProductItemDetailView.as_view(), name='item-detail'),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),
    path('product/add', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
