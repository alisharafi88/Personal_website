# Generated by Django 4.2.13 on 2024-06-16 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0014_rename_skillscategory_skillcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
    ]
