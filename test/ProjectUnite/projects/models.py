from django.db import models
from django.contrib.auth.models import User



CATEGORY_OPTIONS = (
	('All', 'All'),
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
	('All', 'All'),
	('Melbourne', 'Melbourne'),
	('Brunswick', 'Brunswick'),
	('WorldWide', 'WorldWide'),

	)
#sligh modt
class ProjectTitle(models.Model):
	name = models.CharField(max_length = 100)
	user = models.ForeignKey(User)
	projectID = models.AutoField(primary_key=True)


	location = models.CharField(max_length=50, choices = LOCATION_OPTIONS)
	contact_email = models.EmailField()
	description = models.TextField()
	team_members = models.CharField(max_length = 100)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default = True)
	expertise = models.CharField(max_length=50, choices = CATEGORY_OPTIONS)


	def __unicode__(self):
		return self.name


# Create your models here.

#class searchProject(models.Model):
