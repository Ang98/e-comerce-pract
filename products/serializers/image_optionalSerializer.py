from rest_framework import serializers

from products.models import ImageOptional

class ImageOptionalSerializer(serializers.ModelSerializer):

    class Meta:

        model = ImageOptional
        fields = '__all__'