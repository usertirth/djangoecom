from django.shortcuts import render
from .models import product

# Create your views here.
def productdata(request):
    a=product.objects.all()
    return render(request,'product.htm',{'pro':a})