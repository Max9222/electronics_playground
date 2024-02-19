from rest_framework import viewsets

from chain.models import Partner
from chain.serializers.partner import PartnerSerializer
from django_filters import rest_framework as filters

class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contact__country',)
