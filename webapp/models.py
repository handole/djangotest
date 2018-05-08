from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=254)
	slug = models.SlugField(max_length=254)
	image = models.ImageField(upload_to='post/%Y/%m/', blank=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	created_by = models.OneToOneField(settings.AUTH_USER_MODEL, default=1)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title