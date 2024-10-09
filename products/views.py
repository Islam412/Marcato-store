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
        product = self.get_object()
        context["reviews"] = Review.objects.filter(product=product)
        context["average_rating"] = product.average_rating
        context["rate_products"] = Product.objects.filter(brand=product.brand)
        return context
    

class BrandList(ListView):
    model = Brand    
    
