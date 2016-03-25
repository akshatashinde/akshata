from django.db import models

# Create your models here.

class userprof(models.Model):
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	mobileno=models.IntegerField(default=0)
	gender=models.CharField(max_length=200)
	emailid=models.CharField(max_length=200)

	def __unicode__(self):
		return self.fname

class profilepic(models.Model):
	picture = models.ImageField(upload_to='profile_images', blank=True)		

	
