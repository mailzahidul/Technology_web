from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CompanyInfo, Contact, User, Client, TestimonialHeading, Testimonial
from .models import BrandHeading, HomeBanner, WhyChooseUs, Features
# Register your models here.


admin.site.register(User)
admin.site.register(Client)
admin.site.register(BrandHeading)

class TestimonialHeadingAdmin(SummernoteModelAdmin):
    list_display=['title','active']
    summernote_fields = ('sub_title',)
admin.site.register(TestimonialHeading, TestimonialHeadingAdmin)

admin.site.register(Testimonial)
admin.site.register(HomeBanner)
admin.site.register(WhyChooseUs)
admin.site.register(Features)

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
admin.site.register(CompanyInfo, CompanyInfoAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone','email', 'subject', 'time', 'is_response']
    readonly_fields = ['name', 'phone','email', 'subject', 'message']
    list_editable = ['is_response']
admin.site.register(Contact, ContactAdmin)