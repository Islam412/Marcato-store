from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Product, Brand, ProductImage, Review

from django.db import models

class ProductList(ListView):
    model = Product


class ProductDetails(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())        
        context["rate_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    
    
    
