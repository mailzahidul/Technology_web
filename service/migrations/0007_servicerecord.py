# Generated by Django 4.0.2 on 2022-02-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_services_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('icon', models.ImageField(upload_to='services-recor/')),
                ('num_project', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
