from django.db import models
from django.contrib.auth import get_user_model

Posts = get_user_model()
Author = get_user_model()


class Authors(models.Model):
    nickname = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    sex = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=True)


class Posts(models.Model):
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    author = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts'
    )
