from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import ClientSerializer

class ClientView(APIView):

    def post(self, request, *args, **kwargs):
        serializer= LoginEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data={'token':token}
        return Response(data)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
