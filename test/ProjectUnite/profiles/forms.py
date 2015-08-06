from django import forms
from django.contrib.auth.models import User
from .models import SignUp, LOCATION_OPTIONS, CATEGORY_OPTIONS





class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SearchForm(forms.Form):
	location = forms.ChoiceField(LOCATION_OPTIONS)
	expertise = forms.ChoiceField(CATEGORY_OPTIONS)

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		
		fields = ['full_name', 'email','location', 'expertise', 'skills', 'Experience', 'CurrentDegree', 'Currentprojects', 'picture']
		
	def user(self):
		user = SignUp.objects.get(user=user)

		#user = User
		return user

	def clean_email(self):
		email= self.cleaned_data.get('email')
		return email

	def skills(self):
		skills = self.cleaned_data.get('skills')
		return skills

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name
	#def clean_Qualifications(self):
	#	Qualifications = self.cleaned_data.get('Qualifications')
	#	return Qualifications
	def clean_Experience(self):
		Experience = self.cleaned_data.get('Experience')
		return Experience
	def clean_CurrentDegree(self):
		CurrentDegree = self.cleaned_data.get('CurrentDegree')
		return CurrentDegree
	def clean_Currentprojects(self):
		Currentprojects = self.cleaned_data.get('Currentprojects')
		return Currentprojects



#class UserPictureForm(forms.ModelForm):
#	class Meta:
#		model = UserPicture
#		fields = ['image']
