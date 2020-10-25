from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.decorators import action


from products.serializers import ProductSerializer
from products.models import Product,Category,Stock


class ProductLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Product.objects.order_by('-created')[:10]
        lista = ProductSerializer(latest, many=True).data
        return Response(lista)


class ProductOfferLatestView(APIView):

    def get(self, request, *args, **kwargs):
        latest = Product.objects.exclude(
            offer_discount=(0, None)).order_by('-modified')[:10]
        lista = ProductSerializer(latest, many=True).data
        return Response(lista)


class ProductView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self,request):
        
        dic = request.data.dict()
        id_cat = dic.pop('category',None)

        cat = Category.objects.filter(pk=id_cat).first()
        print(cat)
        pro = Product()
        pro.category=cat
        pro.description = dic.pop('description',None)
        pro.display = dic.pop('display',None)
        pro.display_in_home = dic.pop('display_in_home',None)
        pro.name = dic.pop('name',None)
        pro.offer_discount = dic.pop('offer_discount',None)
        pro.order = dic.pop('order',None)
        pro.price = dic.pop('price',None)

        print(dic)

        colors = dic.getlist('color_stocks',None)

        print(colors)


        return Response('Hola :V')

    @action(detail=False, methods=['get'])
    def get_by_slug(self, request):
        slug = request.GET.get('slug', None)
        data = {'detalle': 'Especifique el parametro "slug" '}
        if slug:
            try:
                pro = Product.objects.filter(slug=slug).first()
                data = ProductSerializer(pro, many=True).data
            except Category.DoesNotExist:
                data = {
                    'detalle': 'No se encontro la cateogria con slug {}'.format(slug)}

        return Response(data)
