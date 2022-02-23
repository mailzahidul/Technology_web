from django.db import models

# Create your models here.

class Workflow(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/workflow/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.TextField(max_length=250)
    experince_year = models.PositiveIntegerField()
    quotes = models.TextField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class ProjectStatistics(models.Model):
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='services-recor/')
    num_project = models.IntegerField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class OurSpeciality(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.TextField(max_length=255)
    primary_image = models.ImageField(upload_to='about/', blank=True, null=True)
    secondary_image = models.ImageField(upload_to='about/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    speciality = models.ManyToManyField(OurSpeciality)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class TeamHeading(models.Model):
    section_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.section_name


class Designation(models.Model):
    name = models.CharField(max_length=150) 

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='team', null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    company = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name