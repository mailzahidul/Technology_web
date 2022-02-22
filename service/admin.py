from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceHeading, Services
from .models import ServicePricePackage, ServicePriceCategory, ServicePriceFeature
from .models import ServicePriceHeading, ProjectQuotes
# Register your models here.

admin.site.register(ServiceHeading)

class ServicesAdmin(admin.ModelAdmin):
    list_display=['title','active']

    # def image_tag(self, obj):						   # Image will show on django admin
    #     return format_html('<img src="{}" width="60" height="60" />'.format(obj.bg_image.url))
   
    # image_tag.short_description = 'Image Preview'

admin.site.register(Services, ServicesAdmin)

admin.site.register(ProjectQuotes)

admin.site.register(ServicePriceHeading)
admin.site.register(ServicePriceCategory)
admin.site.register(ServicePriceFeature)
admin.site.register(ServicePricePackage)