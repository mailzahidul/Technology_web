# Generated by Django 4.0.2 on 2022-02-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_servicepriceheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='whychooseus',
            name='sub_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
