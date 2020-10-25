from rest_framework import mixins,viewsets
from rest_framework.response import Response

from products.serializers import ImageOptionalSerializer

from products.models import ImageOptional

class ImageOptionalView(mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):

    queryset = ImageOptional.objects.all()
    serializer_class = ImageOptionalSerializer
