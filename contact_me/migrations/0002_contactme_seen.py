# Generated by Django 4.2.4 on 2023-09-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactme',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
