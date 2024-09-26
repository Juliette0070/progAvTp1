from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

from appTp1.models import Product, ProductItem

# Create your views here.

class HomeView(TemplateView):
    template_name = "appTp1/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        name = self.kwargs.get('name', "DJANGO")
        context['titreh1'] = "Hello " + name
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "appTp1/home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = "appTp1/home.html"
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['titreh1'] = "Contact us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ProductListView(ListView):
    model = Product
    template_name = "appTp1/list_products.html"
    context_object_name = "prdcts"
    def get_queryset(self):
        return Product.objects.order_by('price_ttc')
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des produits"
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "appTp1/detail_product.html"
    context_object_name = "product"
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail produit"
        context['declinaisons'] = ProductItem.objects.filter(product=self.object)
        return context

class ProductItemListView(ListView):
    model = ProductItem
    template_name = "appTp1/list_items.html"
    context_object_name = "declinaisons"
    def get_queryset(self):
        return ProductItem.objects.order_by('code')
    def get_context_data(self, **kwargs):
        context = super(ProductItemListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des déclinaisons"
        return context

class ProductItemDetailView(DetailView):
    model = ProductItem
    template_name = "appTp1/detail_item.html"
    context_object_name = "item"
    def get_context_data(self, **kwargs):
        context = super(ProductItemDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail déclinaison"
        return context

class ConnectView(LoginView):
    template_name = "appTp1/login.html"
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, "appTp1/home.html", {"titreh1": "Hello " + username + ", you're connected"})
        else:
            return render(request, 'appTp1/register.html')
