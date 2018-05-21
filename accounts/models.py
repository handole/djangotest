from django.db import models

# Create your models here.
class Profil(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	username = models.ForeignKey(User, related_name='username')
	email = models.EmailField(max_length=100)
	gender = models.CharField(max_length=30)
	location = models.CharField(max_length=100)
	bio = models.TextField()

	def __str__(self):
		return "%s %s" % (self.lastname, self.firstname)