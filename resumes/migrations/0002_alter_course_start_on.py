# Generated by Django 4.2.4 on 2023-08-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='start_on',
            field=models.IntegerField(choices=[(0, 'soon'), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030)], verbose_name='Start On'),
        ),
    ]