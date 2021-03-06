# Generated by Django 4.0.2 on 2022-02-20 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_whychooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('icon', models.ImageField(upload_to='feature_icon/')),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
