from django.urls import path
from .views import productdata

urlpatterns = [
    path('data/',productdata),

]