from django.contrib import admin
from .models import ProjectTitle


# Register your models here.
#class ProjectAdmin(admin.ModelAdmin):
#	list_display = ["__unicode__", "timestamp", "updated"]
#	form = ProjectForm
#	class Meta:
#		model=SignUp
#admin.site.register(Project, ProjectAdmin)
class ProjectTitleAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","name", "projectID","timestamp", "updated"]
	model= ProjectTitle

#	class Meta:
#		model=SignUp
admin.site.register(ProjectTitle, ProjectTitleAdmin)

