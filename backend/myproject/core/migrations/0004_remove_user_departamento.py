# Generated by Django 2.2.12 on 2020-08-23 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200823_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='departamento',
        ),
    ]