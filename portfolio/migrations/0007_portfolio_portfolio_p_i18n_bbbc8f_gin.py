# Generated by Django 4.2.4 on 2023-09-20 17:27

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_i18n_alter_portfolio_description'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='portfolio',
            index=django.contrib.postgres.indexes.GinIndex(fields=['i18n'], name='portfolio_p_i18n_bbbc8f_gin'),
        ),
    ]
