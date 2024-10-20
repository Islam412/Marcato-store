from django.shortcuts import render
from django.db.models import Count

from products.models import Product , Brand , Review
# Create your views here.

def home(request):
    brands = Brand.objects.all().annotate(products_count=Count('product_name'))
    sale_products = Product.objects.filter(flag='Sale')[:15]
    featured_products = Product.objects.filter(flag='Feature')[:6]
    new_products = Product.objects.filter(flag='New')[:15]
    review = Review.objects.all()[:6]
    
    return render(request, 'settings/home.html', {
        'brands': brands,
        'sale_products': sale_products,
        'featured_products': featured_products,
        'new_products': new_products,
        'review': review
    }) 