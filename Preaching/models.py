from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.


class Preaching(models.Model):
	title_teaching=models.CharField(max_length=350)
	youtube=EmbedVideoField()
	created_on=models.DateTimeField(auto_now_add=True)