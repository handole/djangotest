from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profil(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.OneToOneField(settings.AUTH_USER_MODEL, default=1)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str("%s %s" % (self.lastname, self.firstname))
