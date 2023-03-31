from django.shortcuts import render

# Create your views here.
def products(req):
    return render(req,"products/products.html")