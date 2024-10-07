from django.urls import path
from .views import ProductDetails, ProductList

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetails.as_view(), name='product_detail'),
]
