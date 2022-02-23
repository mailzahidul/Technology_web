from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Tags, Category, Blog, BlogHeading
# Register your models here.


admin.site.register(Tags)
admin.site.register(Category)

class BlogAdmin(SummernoteModelAdmin):
    list_display = ['title', 'get_tags','category']
    summernote_fields = ('description',)


    def get_tags(self, obj):						        # It will show all ManyToMany Data not ForeignKey data
        return ", ".join([p.name for p in obj.tags.all()])

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogHeading)