from rest_framework import mixins,viewsets
from rest_framework.response import Response

from accounts.serializers import ClientSerializer

from accounts.models import Client

class ClientView(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
