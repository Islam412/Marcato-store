# Generated by Django 5.1.1 on 2024-10-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='subtitle',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
