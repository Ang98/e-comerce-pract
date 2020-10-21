from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import password_validation, authenticate


from accounts.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Employee
        fields = '__all__'


class LoginEmployeeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(min_length = 8,max_length = 64)

    def validate(self,data):
        try:
            user = authenticate(username=data['username'],password=data['password'])
            if not user:
                raise serializers.ValidationError('Credenciales Invalidas')
            #employee = Employee.objects.get(user=user)
            self.context['user']=user
        except Employee.DoesNotExist:
            raise serializers.ValidationError('No es un empleado')
        return data
    
    def create(self,data):
        token,created = Token.objects.get_or_create(user=self.context['user'])
        return token.key

    