from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images/')
	pub_date = models.DateTimeField()
	body = models.TextField()