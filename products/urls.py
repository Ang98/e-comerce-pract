from django.urls import path,include

from products.views import ProductView,CategoryView

urlpatterns = [
    path('product/latests/',ProductView.as_view(),name='product_latests'),
    path('category/latests/',CategoryView.as_view(),name='category_latests'),
]