# Generated by Django 4.2.4 on 2023-09-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolio_cover_alter_imgforportfolio_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkforportfolio',
            name='link_domain',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
