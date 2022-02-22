# Generated by Django 4.0.2 on 2022-02-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogheading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogheading',
            old_name='heading',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogheading',
            name='sub_title',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]