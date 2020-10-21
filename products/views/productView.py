from rest_framework.views import APIView
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product

class ProductLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Product.objects.order_by('-created')[:10]
        lista = ProductSerializer(latest,many=True).data
        return Response(lista)

class ProductOfferLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Product.objects.exclude(offer_discount=0).order_by('-modified')[:10]
        lista = ProductSerializer(latest,many=True).data
        return Response(lista)