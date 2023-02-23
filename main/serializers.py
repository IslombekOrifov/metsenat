from rest_framework import (
    serializers
)

from .models import HighEduInstitution


class HighEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighEduInstitution
        fields = ('name',)

