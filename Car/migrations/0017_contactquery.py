# Generated by Django 4.2.6 on 2023-11-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0016_alter_carbooking_no_of_persons'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('loaction', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
