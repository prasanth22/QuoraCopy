from django.db import models
from django.contrib.auth.models import AbstractUser
from topics.models import Topic
# Create your models here.

class QuoraUser(AbstractUser):
	bio = models.CharField(max_length = 128,blank = True,null = True)
	desc = models.TextField(max_length = 8192,blank = True,null=True)
	profile_pic = models.ImageField(upload_to = "/profile_pics",blank = True)
	following_users = models.ManyToManyField("self", symmetrical = False, related_name = "followers")
	following_topics = models.ManyToManyField(Topic,related_name="topic_followers")
