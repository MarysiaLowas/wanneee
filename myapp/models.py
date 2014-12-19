from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
	"""a model representing a tag"""
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	"""a model representing an entry"""
	author = models.ForeignKey(User)
	summary = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	edited_date = models.DateTimeField(default=timezone.now)
	tags = models.ManyToManyField(Tag)	

	def __unicode__(self):
		return self.summary	