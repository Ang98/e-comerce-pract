from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from products.serializers import CategorySerializer
from products.models import Category

from datetime import datetime

class CategoryLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Category.objects.order_by('-created')[:10]
        lista = CategorySerializer(latest,many=True).data
        return Response(lista)

class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    @action(detail=False,methods=['get'])
    def get_by_slug(self,request):
        slug = request.GET.get('slug',None)
        data={'detalle':'Especifique el parametro "slug" '}
        if slug:
            try:
                cat = Category.objects.filter(slug=slug).first()
                data = CategorySerializer(cat).data
            except Category.DoesNotExist:
                data={'detalle':'No se encontro la cateogria con slug {}'.format(slug)}

        return Response(data)
    
    @action(detail=False,methods=['post'])
    def order(self,request):
        lista = request.data.getlist('categories_order_ids',None)
        data={'detalle':'id de cateogrias no encontrados'}
        cats=[]
        for item in lista:
            try:
                cat = Category.objects.get(pk=item)
                cats.append(cat)
            except Category.DoesNotExist:
                data={'detalle':'el id {} no fue encontrado'.format(item)}
                return Response(data)
        data = CategorySerializer(cats,many=True).data

        return Response(data)

