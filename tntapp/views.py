from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.views.generic import *
from .models import *


class ProductListView(ListView):
    template_name = "clienttemplates/packagelist.html"
    queryset = Product.objects.all().order_by('-id')
    context_object_name = "itemlist"
    paginate_by = 6


class ProductDetailView(DetailView):
    template_name = "clienttemplates/packagedetail.html"
    model = Product
    context_object_name = "item"