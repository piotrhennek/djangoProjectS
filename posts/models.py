from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Template(models.Model):
    #title = models.CharField(max_length=200)
    #url = models.TextField()
    #pub_date = models.DateTimeField()
    #author = models.ForeignKey(User)
    #votes_total = models.IntegerField(default=1)

    name = models.CharField(max_length=200)
    text = models.TextField()
    date_creation = models.DateTimeField()
    description = models.TextField()
    version = models.IntegerField(default=1)
    #category =
    access = models.BooleanField()
    user = models.ForeignKey(User)
    #template =
    version_last = models.IntegerField(default=1)

    #def pub_date_pretty(self):
    #   return self.pub_date.strftime('%b %e %Y')

class Tag(models.Model):
    name = models.CharField(max_length=200)
    doc_id = models.IntegerField()
