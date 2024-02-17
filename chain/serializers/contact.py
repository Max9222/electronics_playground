from rest_framework import serializers

from chain.models import Contact
# from chain.serializers.partner import PartnerSerializer


class ContactSerializer(serializers.ModelSerializer):
    # partner = PartnerSerializer(required=False, many=True)

    class Meta:
        model = Contact
        fields = '__all__'
