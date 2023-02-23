from django.db.models import F

from rest_framework import (
    serializers,
    exceptions
)
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from sponsors.models import Sponsor
from sponsors.serializers import SponsorSpentMoneySerializer

from .models import Student, StudentSponsor


class AddSponsorRetrieveSerializer(serializers.ModelSerializer):
    sponsor = SponsorSpentMoneySerializer()
    class Meta:
        model = StudentSponsor
        fields = ('sponsor', 'amount')


class StudentSerializer(serializers.ModelSerializer):
    collected_funts = AddSponsorRetrieveSerializer()
    class Meta:
        model = Student
        fields = (
            'full_name', 'phone', 'contract_amount', 'devided_amount',
            'university', 'student_type', 'collected_funts'
        )
    

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'full_name', 'student_type', 'university', 'devided_amount',
            'contract_amount'
        )


   
class AddSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = ('id','student','sponsor', 'amount')

    def validate(self, attrs):
        if attrs['amount'] > Sponsor.objects.get(pk=attrs['sponsor']).annotate(
            balance=F('donate_amount')-F('spent_money')).balance:
            raise exceptions.ValidationError("Sponsorda bunday mablag' mavjud emas")

    def create(self, validated_data):
        instance = StudentSponsor.objects.create(**validated_data)
        instance.student.devided_amount += instance.amount
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        if instance.sponsor.id != validated_data['sponsor'] or instance.amount != validated_data.amount:
            instance.sponsor.spent_money -= instance.amount
            instance.sponsor.save()
            instance.student.devided_amount -= instance.amount
            instance.student.save()
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)
        instance.sponsor.spent_money = instance.sponsor.spent_money - instance.amount
        instance.sponsor.save()
        instance.student.devided_amount += - instance.amount
        instance.student.save()

        return instance