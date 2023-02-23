from django.shortcuts import render
from django.db.models import F

from rest_framework import (
    permissions,
    viewsets,
    generics
)

from .models import Sponsor
from .serializers import (
    SponsorRegisterSerializer, SponsorListSerializer, SponsorUpdateSerializer,
    SponsorAddDonateSerializer, SponsorRetrieveSerializer
)


class SponsorModelViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.action == 'create':
            return SponsorRegisterSerializer
        elif self.action == 'update':
            return SponsorUpdateSerializer
        elif self.action == 'retrieve':
            return SponsorRetrieveSerializer
        return SponsorListSerializer
    
    
    def get_permissions(self):
        if self.action == 'create':
            return []
        return [permission() for permission in self.permission_classes]
    
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class SponsorAddDonateListApiView(generics.ListAPIView):
    queryset = Sponsor.objects.filter(is_deleted=False).annotate(
        balance=F('donate_amount')-F('spent_money'))
    serializer_class = SponsorAddDonateSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

