from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Workflow, About, OurSpeciality, ProjectStatistics
from .models import Designation, TeamMember, TeamHeading, Experience
# Register your models here.

admin.site.register(Workflow)


class ExperienceAdmin(SummernoteModelAdmin):
    list_display=['title','active']
    summernote_fields = ('title',)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ProjectStatistics)

class AboutAdmin(SummernoteModelAdmin):
    list_display=['title','active']
    summernote_fields = ('sub_title',)

admin.site.register(About, AboutAdmin)
admin.site.register(OurSpeciality)


admin.site.register(TeamHeading)
admin.site.register(Designation)
admin.site.register(TeamMember)