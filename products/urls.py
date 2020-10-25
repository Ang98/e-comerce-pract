from django.urls import path,include

from products.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',CategoryViewset,basename='clientview')
router.register(r'color',ColorViewset,basename='colorview')
router.register(r'stock',StockView,basename='stockview')
router.register(r'image_optional',ImageOptionalView,basename='image_optionalview')
router.register(r'product',ProductView,basename='productview')

urlpatterns = [
    path('product/latests/',ProductLatestView.as_view(),name='product_latests'),
    path('product/offer_latests/',ProductOfferLatestView.as_view(),name='produdct_offer_latests'),
    path('category/latests/',CategoryLatestView.as_view(),name='category_latests'),
    path('color/latests/',ColorLatestView.as_view(),name='color_latests'),
    
    path('',include(router.urls)),
]