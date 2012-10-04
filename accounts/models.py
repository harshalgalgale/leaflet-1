from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user     = models.OneToOneField(User)
	birthday = models.DateField()
	major    = models.CharField(max_length=100, null=True)
	school   = models.CharField(max_length=100, null=True)
