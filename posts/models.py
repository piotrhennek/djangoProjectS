from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Template(models.Model):

    name = models.CharField(max_length=200)
    text = models.TextField()
    date_creation = models.DateTimeField()
    description = models.TextField()
    version = models.IntegerField(default=1)
    access = models.BooleanField()
    user = models.ForeignKey(User)
    version_last = models.IntegerField(default=1)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    doc_id = models.IntegerField()
