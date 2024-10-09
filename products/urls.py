from django.urls import path
from .views import ProductDetails, ProductList, BrandList

app_name = 'products'

urlpatterns = [
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetails.as_view(), name='product_detail'),
]
