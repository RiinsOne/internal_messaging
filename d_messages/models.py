from django.db import models
from django.shortcuts import reverse

from user_model.models import UserModel

from django.utils.text import slugify
from time import time


def gen_slug():
    return str(int(time()))

class Message(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', related_name='t_messages')
    users = models.ManyToManyField('UserModel', related_name='u_messages')
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = gen_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ', ' + self.slug

class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
