from rest_framework import mixins,viewsets
from rest_framework.response import Response

from products.serializers import StockSerializer

from products.models import Stock

class StockView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
