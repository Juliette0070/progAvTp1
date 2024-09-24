from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

from appTp1.models import Product, ProductItem

# Create your views here.

"""def home(request):
    return render(request, "appTp1/home.html")"""

"""def about(request):
    return render(request, "appTp1/about.html")"""

"""def contact(request):
    return render(request, "appTp1/contact.html")"""

"""def hello(request, name):
    return render(request, "appTp1/hello.html", {"name": name})"""

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

def ListProducts(request):
    prdcts = Product.objects.all()
    return render(request, "appTp1/list_products.html", {"prdcts": prdcts})

def ListItemsProduct(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Ce produit n'existe pas")
    declinaisons = ProductItem.objects.filter(product=product)
    return render(request, "appTp1/items.html", {"product": product, "declinaisons": declinaisons})
