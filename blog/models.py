from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from MainApp.models import User


class Tags(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"

class Category(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True, blank=True, null=True)
    sort_description = models.TextField(default='', blank=True, null=True)
    description = models.TextField(default='')
    image = models.FileField(upload_to='post_image/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, blank=True)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.create_date = timezone.now()
        self.update = timezone.now()
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)


class BlogHeading(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    sub_title = models.TextField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title