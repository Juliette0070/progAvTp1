from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy

from appTp1.forms import ContactUsForm, ProductAttributeForm, ProductAttributeValueForm, ProductForm, ProductFournisseurForm, ProductItemForm, FournisseurForm
from appTp1.models import Product, ProductAttribute, ProductAttributeValue, ProductFournisseur, ProductItem, Fournisseur

# View principales

# Home
class HomeView(TemplateView):
    template_name = "appTp1/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        name = self.kwargs.get('name', "DJANGO")
        context['titreh1'] = "Hello " + name
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)


# About
class AboutView(TemplateView):
    template_name = "appTp1/home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)


# Contact
def ContactView(request):
    titreh1 = "Contact us!"
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via MonProjet Contact Us form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monprojet.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "appTp1/contact.html", {"form": form, "titreh1": titreh1})

class EmailSentView(TemplateView):
    template_name = "appTp1/email_sent.html"
    def get_context_data(self, **kwargs):
        context = super(EmailSentView, self).get_context_data(**kwargs)
        context['titreh1'] = "Email sent!"
        return context





# View Authentification

# Login
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

class RegisterView(TemplateView):
    template_name = "appTp1/register.html"
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, "appTp1/login.html")
        else:
            return render(request, 'appTp1/register.html')

class DisconnectView(TemplateView):
    template_name = "appTp1/logout.html"
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)





#View CRUD Models


# View Produit

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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "appTp1/new_product.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "appTp1/update_product.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "appTp1/delete_product.html"
    success_url = reverse_lazy('products')






# View ProductItems

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

class ProductItemCreateView(CreateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "appTp1/new_item.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        item = form.save()
        return redirect('item-detail', item.id)

class ProductItemUpdateView(UpdateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "appTp1/update_item.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        item = form.save()
        return redirect('item-detail', item.id)

class ProductItemDeleteView(DeleteView):
    model = ProductItem
    template_name = "appTp1/delete_item.html"
    success_url = reverse_lazy('items')





# View ProductAttribute

class ProductAttributeListView(ListView):
    model = ProductAttribute
    template_name = "appTp1/list_attributes.html"
    context_object_name = "attributes"
    def get_queryset(self):
        return ProductAttribute.objects.order_by('name')
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des attributs"
        return context

class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = "appTp1/detail_attribute.html"
    context_object_name = "attribute"
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail attribut"
        return context

class ProductAttributeCreateView(CreateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = "appTp1/new_attribute.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        attribute = form.save()
        return redirect('attribute-detail', attribute.id)

class ProductAttributeUpdateView(UpdateView):
    model = ProductAttribute
    form_class = ProductAttributeForm
    template_name = "appTp1/update_attribute.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        attribute = form.save()
        return redirect('attribute-detail', attribute.id)

class ProductAttributeDeleteView(DeleteView):
    model = ProductAttribute
    template_name = "appTp1/delete_attribute.html"
    success_url = reverse_lazy('attributes')





# View ProductAttributeValue

class ProductAttributeValueListView(ListView):
    model = ProductAttributeValue
    template_name = "appTp1/list_values.html"
    context_object_name = "values"
    def get_queryset(self):
        return ProductAttributeValue.objects.order_by('value')
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeValueListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des valeurs"
        return context

class ProductAttributeValueDetailView(DetailView):
    model = ProductAttributeValue
    template_name = "appTp1/detail_value.html"
    context_object_name = "value"
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeValueDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail valeur"
        return context

class ProductAttributeValueCreateView(CreateView):
    model = ProductAttributeValue
    form_class = ProductAttributeValueForm
    template_name = "appTp1/new_value.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        value = form.save()
        return redirect('value-detail', value.id)

class ProductAttributeValueUpdateView(UpdateView):
    model = ProductAttributeValue
    form_class = ProductAttributeValueForm
    template_name = "appTp1/update_value.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        value = form.save()
        return redirect('value-detail', value.id)

class ProductAttributeValueDeleteView(DeleteView):
    model = ProductAttributeValue
    template_name = "appTp1/delete_value.html"
    success_url = reverse_lazy('values')





# View Fournisseur

class FournisseurListView(ListView):
    model = Fournisseur
    template_name = "appTp1/list_fournisseurs.html"
    context_object_name = "fournisseurs"
    def get_queryset(self):
        return Fournisseur.objects.order_by('name')
    def get_context_data(self, **kwargs):
        context = super(FournisseurListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des fournisseurs"
        return context

class FournisseurDetailView(DetailView):
    model = Fournisseur
    template_name = "appTp1/detail_fournisseur.html"
    context_object_name = "fournisseur"
    def get_context_data(self, **kwargs):
        context = super(FournisseurDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail fournisseur"
        return context
    
class FournisseurCreateView(CreateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "appTp1/new_fournisseur.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        fournisseur = form.save()
        return redirect('fournisseur-detail', fournisseur.id)
    
class FournisseurUpdateView(UpdateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "appTp1/update_fournisseur.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        fournisseur = form.save()
        return redirect('fournisseur-detail', fournisseur.id)
    
class FournisseurDeleteView(DeleteView):
    model = Fournisseur
    template_name = "appTp1/delete_fournisseur.html"
    success_url = reverse_lazy('fournisseurs')





# View ProductFournisseur

class ProductFournisseurListView(ListView):
    model = ProductFournisseur
    template_name = "appTp1/list_productsfournisseurs.html"
    context_object_name = "productsfournisseurs"
    def get_queryset(self):
        return ProductFournisseur.objects.order_by('product')
    def get_context_data(self, **kwargs):
        context = super(ProductFournisseurListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des produits de fournisseurs"
        return context

class ProductFournisseurDetailView(DetailView):
    model = ProductFournisseur
    template_name = "appTp1/detail_productfournisseur.html"
    context_object_name = "productfournisseur"
    def get_context_data(self, **kwargs):
        context = super(ProductFournisseurDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail fournisseur"
        return context
    
class ProductFournisseurCreateView(CreateView):
    model = ProductFournisseur
    form_class = ProductFournisseurForm
    template_name = "appTp1/new_productfournisseur.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        productfournisseur = form.save()
        return redirect('productfournisseur-detail', productfournisseur.id)
    
class ProductFournisseurUpdateView(UpdateView):
    model = ProductFournisseur
    form_class = ProductFournisseurForm
    template_name = "appTp1/update_productfournisseur.html"
    def form_valid(self, form:BaseModelForm)->HttpResponse:
        productfournisseur = form.save()
        return redirect('productfournisseur-detail', productfournisseur.id)
    
class ProductFournisseurDeleteView(DeleteView):
    model = ProductFournisseur
    template_name = "appTp1/delete_productfournisseur.html"
    success_url = reverse_lazy('productsfournisseurs')
