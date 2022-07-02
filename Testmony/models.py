from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.


class Youtube(models.Model):
	Name=models.CharField(max_length=250)
	sub_Title=models.CharField(max_length=250)
	Video=EmbedVideoField()
