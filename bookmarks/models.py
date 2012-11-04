from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
	url = models.URLField(unique=True)
	def __unicode__ (self):
		return self.url

class BookmarkList(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=200)
	picture = models.FileField(upload_to='projects')
	link = models.ForeignKey(Link)
	type = models.IntegerField(default=1)
	date = models.DateTimeField(auto_now_add=True)
	votes = models.IntegerField(default=0)
	def __unicode__ (self):
		return u'%s, %s' % (self.link.url)