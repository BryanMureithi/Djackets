from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            'price',
            'get_thumbnail',
            'get_image'
        )
