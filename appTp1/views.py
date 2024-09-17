from django.shortcuts import render
from django.http import HttpResponse

from appTp1.models import Product, ProductItem

# Create your views here.

def home(request):
    return render(request, "appTp1/home.html")

def contact(request):
    return render(request, "appTp1/contact.html")

def about(request):
    return render(request, "appTp1/about.html")

def hello(request, name):
    return render(request, "appTp1/hello.html", {"name": name})

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
