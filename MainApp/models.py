from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a Password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fast_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    img = models.ImageField(upload_to='user', default='')
    password = models.CharField(max_length=90)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_fullname(self):
        return self.fast_name + " " + self.last_name


class HomeBanner(models.Model):
    title = models.CharField(max_length=250)
    choose_blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, blank=True, null=True)
    choose_project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, blank=True, null=True)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title


DAYS = (
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday')
)

class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(max_length=50)
    alt_phone = PhoneNumberField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=150)
    website = models.URLField(default="https://bitspirits.io/", null=True, blank=True)
    address = models.CharField(max_length=250)
    title = models.CharField(max_length=250, default="Bit Spirits Ltd. || Your best choice")
    sub_title = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(max_length=1000, default="", null=True, blank=True)
    descriptions = models.TextField(max_length=1000, default="", null=True, blank=True)
    fav_icon = models.ImageField(upload_to='company')
    header_logo = models.ImageField(upload_to='company', null=True, blank=True)
    footer_logo = models.ImageField(upload_to='company', default="", null=True, blank=True)
    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    linkedin = models.CharField(max_length=250, default="", null=True, blank=True)
    google_map_url = models.URLField(default="", null=True, blank=True)
    video_img = models.ImageField(upload_to='company', default="", null=True, blank=True)
    opening_day = models.CharField(max_length=250, choices=DAYS, null=True, blank=True)
    opening_time = models.TimeField(max_length=50, null=True, blank=True)
    video = models.URLField(max_length=250, default="", null=True, blank=True)
    holiday = MultiSelectField(max_length=100, choices=DAYS, default="", null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_response = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='client/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_logo = models.ImageField(upload_to='client_company/', null=True, blank=True)
    phone = PhoneNumberField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    website = models.URLField(default="https://bitspirits.io/", null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class BrandHeading(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    sub_title = models.CharField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class TestimonialHeading(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='', null=True, blank=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='why_choose_us/')
    bg_image = models.ImageField(upload_to='why_choose_us/')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title



class Features(models.Model):
    title = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='feature_icon/')
    description = models.TextField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
