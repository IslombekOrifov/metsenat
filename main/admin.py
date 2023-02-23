from django.contrib import admin

from .models import HighEduInstitution

@admin.register(HighEduInstitution)
class HighEduInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')