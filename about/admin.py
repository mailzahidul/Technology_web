from django.contrib import admin
from .models import Workflow, About, OurSpeciality, ProjectStatistics
from .models import Designation, TeamMember, TeamHeading, Experience
# Register your models here.

admin.site.register(Workflow)
admin.site.register(Experience)
admin.site.register(ProjectStatistics)
admin.site.register(About)
admin.site.register(OurSpeciality)


admin.site.register(TeamHeading)
admin.site.register(Designation)
admin.site.register(TeamMember)