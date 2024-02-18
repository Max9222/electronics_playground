
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from chain.models import Partner
from chain.serializers.contact import ContactSerializer

from chain.serializers.product import ProductSerializer


class PartnerSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(source='contact_set', many=True)
    product = ProductSerializer(required=False, many=True)
    early_partner = serializers.SlugRelatedField(slug_field='title', queryset=Partner.objects.all())

    class Meta:
        model = Partner
        fields = ('title', 'contact', 'product', 'early_partner', 'backlog', 'date_create',)
