# Generated by Django 4.2.6 on 2023-11-07 11:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0011_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='capacity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='addcar',
            name='rent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
