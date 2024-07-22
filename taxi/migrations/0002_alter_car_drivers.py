# Generated by Django 5.0.7 on 2024-07-22 13:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(related_name='drivers', to=settings.AUTH_USER_MODEL),
        ),
    ]
