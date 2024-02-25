from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from chain.models import Partner
from chain.permissions.partner import IsModerator
from chain.serializers.partner import PartnerSerializer
from django_filters import rest_framework as filters


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('contact__country',)

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsModerator]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

