from django.shortcuts import render
from .models import Products
# Create your views here.
def products(req):
    return render(req,"products/products.html", {"productsDB": Products.objects.all()})