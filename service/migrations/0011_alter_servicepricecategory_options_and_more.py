# Generated by Django 4.0.2 on 2022-02-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_servicepricecategory_servicepricefeature_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicepricecategory',
            options={'verbose_name_plural': 'Servicec Price Categories'},
        ),
        migrations.AddField(
            model_name='servicepricecategory',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
