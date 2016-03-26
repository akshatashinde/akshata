from django.db import models
from PIL import Image
from django.db.models import signals
from django.contrib.auth.models import User

# Create your models here.
def create_user(sender, instance, created, **kwargs):
	print "save is called"
		
class userprof(models.Model):
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	mobileno=models.IntegerField(default=0)
	gender=models.CharField(max_length=200)
	emailid=models.CharField(max_length=200)

	def __unicode__(self):
		return self.fname

class UserProfile(models.Model):
	user1 = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user1.username

class profilepic(models.Model):
	picture = models.ImageField(upload_to='profile_images', blank=True)		

signals.post_save.connect(create_user, sender=UserProfile)
