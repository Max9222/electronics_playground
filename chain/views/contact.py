from rest_framework import viewsets

from chain.models import Contact
from chain.serializers.contact import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
