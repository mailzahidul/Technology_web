from django.db import models
from blog.models import Category, Tags
from django.utils.text import slugify
from MainApp.models import Client
# Create your models here.

# On working
class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    project_url = models.URLField(max_length=250, null=True, blank=True)
    short_description = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(upload_to='project')
    logo = models.ImageField(upload_to='project', default='', null=True, blank=True)
    description = models.TextField(default='',null=True, blank=True)
    complete_data = models.DateField(null=True, blank=True)
    billing_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    view_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    active = models.BooleanField(default=True)

    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    linkedin = models.CharField(max_length=250, default="", null=True, blank=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Project, self).save(*args, **kwargs)


class ProjectHeading(models.Model):
    title = models.TextField(max_length=250, null=True, blank=True)
    sub_title = models.TextField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

