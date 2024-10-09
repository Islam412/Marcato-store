from django.urls import path
from .views import ProductDetails, ProductList, BrandList

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetails.as_view(), name='product_detail'),
    path('brand/', BrandList.as_view(), name='brand_list'),
]
