# Generated by Django 4.0.2 on 2022-02-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('icon', models.ImageField(upload_to='services-recor/')),
                ('num_project', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
