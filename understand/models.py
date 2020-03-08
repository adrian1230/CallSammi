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
	source = models.CharField(max_length=100)
	original_text = models.TextField()
	summarized_text = models.CharField(max_length=10000)
	category = models.CharField(max_length=70, choices=categories, default="NA", null=True, blank=True)
	user = models.CharField(max_length=100, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
