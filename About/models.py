from django.db import models

# Create your models here.

class About(models.Model):
	title=models.CharField(max_length=35000)
	Description=models.TextField()
	Photo=models.ImageField(upload_to='About_photo/',blank=False,null=False)

