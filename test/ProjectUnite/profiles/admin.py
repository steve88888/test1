from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	model= SignUp
#	class Meta:
#		model=SignUp
admin.site.register(SignUp, SignUpAdmin)

#class UserPictureAdmin(admin.ModelAdmin):
#	list_display = ["__unicode__", "timestamp"]
#	class Meta:
#		form = SignUpForm
#	class Meta:
#		model=UserPicture
#admin.site.register(UserPicture, UserPictureAdmin)