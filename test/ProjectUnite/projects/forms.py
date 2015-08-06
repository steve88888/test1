from django import forms

from .models import ProjectTitle, LOCATION_OPTIONS, CATEGORY_OPTIONS


class SearchForm(forms.Form):
	location = forms.ChoiceField(LOCATION_OPTIONS)
	expertise = forms.ChoiceField(CATEGORY_OPTIONS)
	
class DeleteForm(forms.Form):
	projectID = forms.IntegerField();
	
class FormProjectTitle(forms.ModelForm):
	class Meta:
		model = ProjectTitle
		fields = ['name', 'location', 'expertise','contact_email', 'description', 'team_members']
	
	def clean_title(self):
		title = self.cleaned_data.get('title')
		return title

	def clean_description(self):
		description = self.cleaned_data.get('description')
		return description

	def clean_title(self):
		team_members = self.cleaned_data.get('team_members')
		return team_members

	
	