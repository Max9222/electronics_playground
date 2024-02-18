from rest_framework import viewsets

from chain.models import Contact
from chain.serializers.contact import ContactSerializer
from django_filters import rest_framework as filters


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city',)
