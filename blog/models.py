from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(blank=True)
    author = models.ForeignKey(User, models.CASCADE)


    def __str__(self):
        return "{}::{}".format(self.title, self.author)
