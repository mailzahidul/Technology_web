# Generated by Django 4.0.2 on 2022-02-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_client_testimonial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='heading',
        ),
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]