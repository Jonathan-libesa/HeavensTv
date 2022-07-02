from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.


class Youtube(models.Model):
	Title=models.CharField(max_length=250)
	Video=EmbedVideoField()
	created_on=models.DateTimeField(auto_now_add=True)

class Page(models.Model):
	Title=models.CharField(max_length=350)
	Description=models.TextField()
	image=models.ImageField(upload_to='Heavens_photo/',blank=False,null=False) 
	created_on=models.DateTimeField(auto_now_add=True)



	