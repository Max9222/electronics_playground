from rest_framework import viewsets

from chain.models import Partner
from chain.serializers.partner import PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
