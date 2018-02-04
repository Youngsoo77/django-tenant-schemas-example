# Generated by Django 2.0.2 on 2018-02-04 02:59

from django.contrib.auth.models import User
from django.db import migrations


def create_admin(apps, schema_editor):
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
