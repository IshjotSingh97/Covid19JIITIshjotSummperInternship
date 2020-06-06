from django.db import models

# Create your models here.
class Myth(models.Model):
	title = models.TextField(max_length=200)
    img = models.URLField(max_length=200)

