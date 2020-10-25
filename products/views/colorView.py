from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from products.serializers import ColorSerializer
from products.models import Color

class ColorLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Color.objects.order_by('-created')[:10]
        lista = ColorSerializer(latest,many=True).data
        return Response(lista)

class ColorViewset(viewsets.ModelViewSet):

    queryset = Color.objects.all()
    serializer_class = ColorSerializer