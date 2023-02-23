# Generated by Django 3.2 on 2023-02-23 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sponsors', '0002_rename_is_delete_sponsor_is_deleted'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentSponsors',
            new_name='StudentSponsor',
        ),
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]