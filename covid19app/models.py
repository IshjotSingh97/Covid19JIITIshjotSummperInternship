from django.db import models

# Create your models here.
class Myth(models.Model):
	title = models.CharField(max_length=200)
	subject = models.TextField(max_length=1000)

class Comment(models.Model):
	title = models.CharField(max_length=200)
	user = models.CharField(max_length=200)