from rest_framework import serializers

from chain.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('email', 'country', 'city', 'street', 'house_number',)
