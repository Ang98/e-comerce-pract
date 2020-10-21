from rest_framework.views import APIView
from rest_framework.response import Response

from products.serializers import CategorySerializer
from products.models import Category

from datetime import datetime

class CategoryView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Category.objects.order_by('-created')[:10]
        lista = CategorySerializer(latest,many=True).data
        return Response(lista)