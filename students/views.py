from django.shortcuts import get_object_or_404 as _get_object_or_404
from django.http import Http404
from django.core.exceptions import ValidationError

from rest_framework import (
    permissions,
    viewsets
)

from .models import Student, StudentSponsor
from .serializers import (
    StudentSerializer, StudentListSerializer,
    AddSponsorSerializer
)


def get_object_or_404(queryset, *filter_args, **filter_kwargs):
    """
    Same as Django's standard shortcut, but make sure to also raise 404
    if the filter_kwargs don't match the required types.
    """
    try:
        return _get_object_or_404(queryset, *filter_args, **filter_kwargs)
    except (TypeError, ValueError, ValidationError):
        raise Http404
    

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(is_deleted=False)
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
       
        if self.action == 'retrieve':
            obj = Student.objects.filter(
                is_deleted=False, **filter_kwargs
            ).prefetch_related('collected_funts').select_related(
                'collected_funts__sponsor'
            ).get()
            if not obj:
                raise Http404('No matches the given query.')
        else:
            obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        return StudentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class AddSponsorModelViewSet(viewsets.ModelViewSet):
    queryset = StudentSponsor.objects.all()
    serializer_class = AddSponsorSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    
    
    def perform_destroy(self, instance):
        # instance.student.devided_amount -= instance.amount
        # instance.student.save()
        instance.sponsor.spent_money -= instance.amount
        instance.sponsor.save()
        instance.delete()


