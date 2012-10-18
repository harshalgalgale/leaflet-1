from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user     = models.OneToOneField(User)
	birthday = models.DateField()
	major    = models.CharField(max_length=100, null=True, blank=True)
	school   = models.CharField(max_length=100, null=True, blank=True)
	fav_subj = models.CharField(max_length=100, null=True, blank=True, verbose_name="Favorite Subject")
	leaves   = models.IntegerField(null=True, default=0)
	votes    = models.IntegerField(null=True, default=0)

	def __unicode__(self):
		return unicode(self.user)