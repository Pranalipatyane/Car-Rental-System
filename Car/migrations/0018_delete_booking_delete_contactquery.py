# Generated by Django 4.2.6 on 2023-11-18 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0017_contactquery'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='ContactQuery',
        ),
    ]
