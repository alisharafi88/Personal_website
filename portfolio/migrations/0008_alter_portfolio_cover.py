# Generated by Django 4.2.4 on 2024-06-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_portfolio_portfolio_p_i18n_bbbc8f_gin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='cover',
            field=models.ImageField(upload_to='portfolio'),
        ),
    ]
