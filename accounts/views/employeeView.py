from rest_famework.views import APIView
from rest_framework.response import Response
from serializers import EmployeeSerializer,LoginEmployeeSerializer

class LoginEmployee(APIView):

    def post(self, request, *args, **kwargs):
        serializer= LoginEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data={'token_key':token}
        return Response(data)


        