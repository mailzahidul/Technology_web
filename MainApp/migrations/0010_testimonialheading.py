# Generated by Django 4.0.2 on 2022-02-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_remove_testimonial_heading_alter_client_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]