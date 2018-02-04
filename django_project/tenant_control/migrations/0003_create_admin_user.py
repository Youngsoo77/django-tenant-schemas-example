# Generated by Django 2.0.2 on 2018-02-04 17:38

from django.contrib.auth.models import User
from django.db import migrations


def create_admin(apps, schema_editor):
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_control', '0002_create_public_tenant'),
        ('auth', '0009_alter_user_last_name_max_length')
    ]

    operations = [
        migrations.RunPython(create_admin)
    ]
