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

from appTp1.forms import ContactUsForm, ProductForm, ProductItemForm
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
