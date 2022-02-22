from django.db import models

# Create your models here.



class ServiceHeading(models.Model):
    heading = models.TextField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading


class Services(models.Model):
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='services/')
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    bg_image = models.ImageField(upload_to='services/', null=True, blank=True)
    description = models.TextField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProjectQuotes(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ServicePriceHeading(models.Model):
    title = models.TextField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class ServicePriceCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='services/icon/', blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    is_popular = models.BooleanField(default=True)
    is_recomended = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Servicec Price Categories"

# On working  
class ServicePriceFeature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# On working  
PACKAGE=(
    ('monthly','Monthly'),
    ('anully','Anully'),
)

# On working
class ServicePricePackage(models.Model):
    price = models.PositiveIntegerField()
    package = models.CharField(max_length=50, choices=PACKAGE, blank=True, null=True)
    price_category = models.ForeignKey(ServicePriceCategory, on_delete=models.CASCADE)
    features = models.ManyToManyField(ServicePriceFeature, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{str(self.price)} for {self.package}"

