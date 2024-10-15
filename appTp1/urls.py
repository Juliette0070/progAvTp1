from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<name>', views.HomeView.as_view(), name='home'),

    path('about/', views.AboutView.as_view(), name='about'),

    path('contact/', views.ContactView, name='contact'),
    path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path('product/list', views.ProductListView.as_view(), name='products'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/add', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    path('item/list', views.ProductItemListView.as_view(), name='items'),
    path('item/<pk>/', views.ProductItemDetailView.as_view(), name='item-detail'),
    path('item/add', views.ProductItemCreateView.as_view(), name='item-add'),
    path('item/<pk>/update/', views.ProductItemUpdateView.as_view(), name='item-update'),
    path('item/<pk>/delete/', views.ProductItemDeleteView.as_view(), name='item-delete'),

    path('attribute/list', views.ProductAttributeListView.as_view(), name='attributes'),
    path('attribute/<pk>/', views.ProductAttributeDetailView.as_view(), name='attribute-detail'),
    path('attribute/add', views.ProductAttributeCreateView.as_view(), name='attribute-add'),
    path('attribute/<pk>/update/', views.ProductAttributeUpdateView.as_view(), name='attribute-update'),
    path('attribute/<pk>/delete/', views.ProductAttributeDeleteView.as_view(), name='attribute-delete'),

    path('value/list', views.ProductAttributeValueListView.as_view(), name='values'),
    path('value/<pk>/', views.ProductAttributeValueDetailView.as_view(), name='value-detail'),
    path('value/add', views.ProductAttributeValueCreateView.as_view(), name='value-add'),
    path('value/<pk>/update/', views.ProductAttributeValueUpdateView.as_view(), name='value-update'),
    path('value/<pk>/delete/', views.ProductAttributeValueDeleteView.as_view(), name='value-delete'),

    path('fournisseur/list', views.FournisseurListView.as_view(), name='fournisseurs'),
    path('fournisseur/<pk>/', views.FournisseurDetailView.as_view(), name='fournisseur-detail'),
    path('fournisseur/add', views.FournisseurCreateView.as_view(), name='fournisseur-add'),
    path('fournisseur/<pk>/update/', views.FournisseurUpdateView.as_view(), name='fournisseur-update'),
    path('fournisseur/<pk>/delete/', views.FournisseurDeleteView.as_view(), name='fournisseur-delete'),

    path('commande/list', views.CommandeListView.as_view(), name='commandes'),
    path('commande/<pk>/', views.CommandeDetailView.as_view(), name='commande-detail'),
    path('commande/add', views.CommandeCreateView.as_view(), name='commande-add'),
    path('commande/<pk>/update/', views.CommandeUpdateView.as_view(), name='commande-update'),
    path('commande/<pk>/delete/', views.CommandeDeleteView.as_view(), name='commande-delete'),

    path('productfournisseur/list', views.ProductFournisseurListView.as_view(), name='productsfournisseurs'),
    path('productfournisseur/<pk>/', views.ProductFournisseurDetailView.as_view(), name='productfournisseur-detail'),
    path('productfournisseur/add', views.ProductFournisseurCreateView.as_view(), name='productfournisseur-add'),
    path('productfournisseur/<pk>/update/', views.ProductFournisseurUpdateView.as_view(), name='productfournisseur-update'),
    path('productfournisseur/<pk>/delete/', views.ProductFournisseurDeleteView.as_view(), name='productfournisseur-delete'),
]
