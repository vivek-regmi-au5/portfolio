from django.db import models

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
	summary = models.CharField(max_length=200)