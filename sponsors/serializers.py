from rest_framework import (
    serializers
)

from .models import Sponsor


class SponsorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'full_name', 'phone', 'donate_amount', 'is_legal_entity',
            'organization',
        )

class SponsorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'full_name', 'phone', 'donate_amount', 'donate_type', 'status', 'is_legal_entity',
            'organization',
        )


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = (
            'full_name', 'phone', 'donate_amount', 'spent_money',
            'date_created', 'status'
        )


class SponsorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        exclude = ('spent_money', 'is_delete', 'date_created', 'date_updated')
        

class SponsorAddDonateSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField()
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'banalce')


class SponsorSpentMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'full_name')
       