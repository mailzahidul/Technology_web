# Generated by Django 4.0.2 on 2022-02-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesection',
            name='sub_title',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='servicesection',
            name='title',
            field=models.TextField(max_length=250),
        ),
    ]
