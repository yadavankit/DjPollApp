from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
	#Unicode for Question
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	#Was Published Recently
	def wasPublishedRecently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
	#Unicode for Choice
	def __str__(self):
		return self.choice_text
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


						