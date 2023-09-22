# Generated by Django 4.2.4 on 2023-09-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_linkforportfolio_link_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='cover',
            field=models.ImageField(default=2, upload_to='portfolio/%Y/%m'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imgforportfolio',
            name='img',
            field=models.ImageField(upload_to='covers/portfolio/%Y/%m'),
        ),
    ]