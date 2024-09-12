from django.shortcuts import render
from django.http import HttpResponse

from appTp1.models import Product, ProductItem

# Create your views here.

def home(request):
    return HttpResponse(
        "<h1>Hello Django!</h1>"
        "<a href='/appTp1/contact'>Contact</a> - <a href='/appTp1/about'>About</a> - <a href='/appTp1/hello/you'>Hello</a> - <a href='/appTp1/products'>Products</a>"
    )

def contact(request):
    return HttpResponse(
        "<h1>Contact us</h1>"
        "<a href='/appTp1/'>Home</a>"
    )

def about(request):
    return HttpResponse(
        "<h1>About us</h1>"
        "<a href='/appTp1/'>Home</a>"
    )

def hello(request, name):
    return HttpResponse(
        f"<h1>Hello {name}!</h1>"
        "<a href='/appTp1/'>Home</a>"
    )

def ListProducts(request):
    prdcts = Product.objects.all()
    liste_prdts = ""
    for p in prdcts:
        liste_prdts += "<li><a href='/appTp1/items/"+str(p.id)+"'>"+p.name+" ("+str(p.price_ht)+"€)"+"</a></li>"
    if liste_prdts == "":
        liste_prdts = "<li>Aucun produit</li>"
    return HttpResponse(
        "<h1>Liste des produits</h1>"
        "<a href='/appTp1/'>Home</a>"
        "<p>Liste des produits:</p>"
        "<ul>"
        f"{liste_prdts}"
        "</ul>"
    )

def ListItemsProduct(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Ce produit n'existe pas")
    prdcts = ProductItem.objects.filter(product=product)
    liste_prdts = ""
    for p in prdcts:
        liste_prdts += "<li style='color:"+p.color+"';>"+p.color+"</li>"
    if liste_prdts == "":
        liste_prdts = "<li>Aucune déclinaison</li>"
    return HttpResponse(
        "<h1>Produit: "+product.name+"</h1>"
        "<a href='/appTp1/'>Home</a> - <a href='/appTp1/products'>Products</a>"
        "<p>Prix HT: "+str(product.price_ht)+"€</p>"
        "<p>Date de fabrication: "+str(product.date_creation)+"</p>"
        "<p>Liste des déclinaisons du produit:</p>"
        "<ul>"
        f"{liste_prdts}"
        "</ul>"
    )
