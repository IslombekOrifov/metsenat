# Generated by Django 3.2 on 2023-02-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]