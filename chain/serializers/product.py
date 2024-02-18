from rest_framework import serializers

from chain.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'date_start',)
