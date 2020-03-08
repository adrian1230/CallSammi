from __future__ import unicode_literals
from django.db import models

categories = (
	('healthcare','healthcare'),
	('technology','technology'),
	('science','science'),
	('beauty','beauty'),
	('entertainment','entertainment'),
	('politic','politic'),
	('culinary','culinary'),
	('others','others')
)

class Result(models.Model):
	title = models.CharField(max_length=40, null=True,blank=True)
	source = models.CharField(max_length=100, null=True, blank=True)
	original_text = models.TextField()
	summarized_text = models.TextField(null=True, blank=True)
	category = models.CharField(max_length=70, choices=categories)
	user = models.CharField(max_length=100,null=True,blank=True)
	date = models.DateTimeField(auto_now_add=True)
