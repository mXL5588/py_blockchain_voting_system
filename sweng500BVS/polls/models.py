from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(models.Model):
	question = models.ForeignKey(Question, on delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

#class Ballot(models.Model):
#	ballot_text = models.CharField(max_length=200)
#	pub_date = models.DateTimeField('date published')
#	end_date = models.DateTimeField('end date')

#class Candidate(models.Model):
#	ballot = models.ForeignKey(Ballot, on delete=models.CASCADE)
#	candidate_text = models.CharField(max_length=100)
#	candidate_address = models.CharField(max_length=36)
#	votes = models.IntegerField(default=0)

	


