from django.urls import path,include

from products.views import ProductLatestView,CategoryLatestView,ColorLatestView,ProductOfferLatestView

urlpatterns = [
    path('product/latests/',ProductLatestView.as_view(),name='product_latests'),
    path('product/offer_latests/',ProductOfferLatestView.as_view(),name='produdct_offer_latests'),
    path('category/latests/',CategoryLatestView.as_view(),name='category_latests'),
    path('color/latests/',ColorLatestView.as_view(),name='color_latests'),
]