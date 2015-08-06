from django.db import models
from django.contrib.auth.models import User


CATEGORY_OPTIONS = (
	('Business and Commerce', 'Business and Commerce'),
	('Architecture, Construction, Urban Design', 'Architecture, Construction, Urban Design'),
	('Fashion & Style', 'Fashion & Style'),
	('Computer Science and Information Technology', 'Computer Science and Information Technology'),
	('Healthcare','Healthcare'),
	('Retail & Sales','Retail & Sales'),
	('Food & Restaurant', 'Food & Restaurant'),
	('Charity and fundraising organising', 'Charity and fundraising organising'),
	('Research and Thesis', 'Research and Thesis'),
	)

LOCATION_OPTIONS = (
	('Melbourne', 'Melbourne'),
	('Brunswick', 'Brunswick'),
	('WorldWide', 'WorldWide'),
)

class SignUp(models.Model):
	#user = models.ForeignKey(SignUp)
	email = models.EmailField()
	user = models.ForeignKey(User)
	userID = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=40)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, null = True, blank = True)
	expertise = models.CharField(max_length = 50, choices = CATEGORY_OPTIONS)
	location = models.CharField(max_length=50, choices = LOCATION_OPTIONS)
		#might need text widget
	skills = models.TextField()
		#Qualifications = models.TextField()
	Experience = models.TextField()
	CurrentDegree = models.CharField(max_length=40, blank = True, null = True)
	Currentprojects = models.TextField()

	active = models.BooleanField(default = True)
	#picture = models.ImageField(upload_to=upload_location, null)
	picture = models.ImageField(upload_to="images/", null = True, blank = True)
	def __unicode__(self):
		return self.full_name
# Create your models here.

#class SearchProfiles(models.Model):

#class UserPicture(models.Model):
#	user = models.ForeignKey(User)
#	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#	active = models.BooleanField(default = True)
#	thumbnail = models.BooleanField(default = False)
#	def __unicode__(self):
#		return str(self.image)
