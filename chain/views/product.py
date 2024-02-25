from rest_framework import viewsets
from chain.models import Product
from chain.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
