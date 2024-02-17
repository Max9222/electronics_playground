
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from chain.models import Partner, Contact
from chain.serializers.contact import ContactSerializer

from chain.serializers.product import ProductSerializer


class PartnerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=False, many=True)
    product = ProductSerializer(required=False, many=True)
    title = SlugRelatedField(slug_field='title', queryset=Contact.objects.all())

    class Meta:
        model = Partner
        fields = '__all__'
