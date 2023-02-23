from django.shortcuts import render
from django.db.models import Subquery, Sum

from rest_framework import (
    viewsets,
    permissions,
    generics,
    response
)

from sponsors.models import Sponsor
from students.models import Student

from .models import HighEduInstitution
from .serializers import HighEduSerializer


class HeiModelViewSet(viewsets.ModelViewSet):
    queryset = HighEduInstitution.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = HighEduSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.users)



class Dashboard(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        amounts = Student.objects.filter(is_deleted=False).aggregate(
            payed=Sum('devided_amount'), needed=Sum('contract_amount')
        )
        user = request.user.username
        return response.Response({'amounts': amounts, 'username': user})


