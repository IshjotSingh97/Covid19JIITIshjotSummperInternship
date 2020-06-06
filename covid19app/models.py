from django.db import models

# Create your models here.
class Myth(models.Model):
	models.TextField(max_length=200)
    models.URLField(max_length=200)

