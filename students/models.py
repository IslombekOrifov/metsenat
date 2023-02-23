from django.db import models
from django.core.validators import MinValueValidator

from accounts.models import CustomUser
from main.models import HighEduInstitution
from sponsors.models import Sponsor
from sponsors.validators import validate_phone

from .enums import StudentType


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13, blank=True, validators=[validate_phone])

    contract_amount = models.FloatField(default=0, validators=[MinValueValidator(0)])
    devided_amount = models.FloatField(default=0, validators=[MinValueValidator(0)])

    university = models.ForeignKey(HighEduInstitution, related_name='students', on_delete=models.PROTECT)
    student_type = models.CharField(max_length=1, choices=StudentType.choices(), default=StudentType.b.name)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    author = models.ForeignKey(CustomUser, related_name='students', on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.full_name = ' '.join(self.full_name.strip().split())
        super().save(*args, **kwargs)


class StudentSponsor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='collected_funts')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT, related_name='spent_funts')
    amount = models.FloatField(validators=[MinValueValidator(0)])
    date_created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(CustomUser, related_name='collect_moneys', on_delete=models.SET_NULL, null=True)
