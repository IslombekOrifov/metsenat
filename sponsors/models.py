from django.db import models
from django.core.validators import MinValueValidator

from .validators import validate_phone
from .enums import SponsorStatus, PayType


class Sponsor(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=13, blank=True, validators=[validate_phone])

    donate_amount = models.FloatField(default=0, validators=[MinValueValidator(0)])
    donate_type = models.CharField(max_length=1, choices=PayType.choices(), blank=True)
    spent_money = models.FloatField(default=0, validators=[MinValueValidator(0)])

    is_legal_entity = models .BooleanField(default=False)
    organization = models.CharField(max_length=200, blank=True)

    status = models.CharField(max_length=1, choices=SponsorStatus.choices(), default=SponsorStatus.n.name)
    is_deleted = models.BooleanField(default=False)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    
    def save(self, *args, **kwargs):
        self.full_name = ' '.join(self.full_name.strip().split())
        super().save(*args, **kwargs)