# Generated by Django 4.0.2 on 2022-02-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_designation_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]
