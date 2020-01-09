from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.utils.text import slugify
from time import time
from django.shortcuts import render


class UserModelManager(BaseUserManager):
    def create_user(self, username, fullname, entity, password=None):
        if not username:
            raise ValueError('User must have an username.')
        if not fullname:
            raise ValueError('User must have a fullname.')
        if not entity:
            raise ValueError('User must have an entity.')

        user = self.model(
            username=username.lower(),
            fullname=fullname.title(),
            entity=entity.upper()
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, fullname, entity, password):
        user = self.create_user(
            username=username.lower(),
            password=password,
            fullname=fullname.title(),
            entity=entity.upper()
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=30, unique=True)
    fullname = models.CharField(verbose_name='full name', max_length=100)
    entity = models.CharField(verbose_name='entity', max_length=60)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fullname', 'entity']

    objects = UserModelManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.fullname = self.fullname.title()
        self.entity = self.entity.upper()
        super(UserModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Create User'
        verbose_name_plural = 'Create Users'


def gen_slug():
    return str(int(time()))


class Message(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    # body = models.TextField(blank=True, db_index=True)
    body = models.TextField(db_index=True)
    tags = models.ManyToManyField('Tag', related_name='t_messages')
    users = models.ManyToManyField('UserModel', related_name='u_messages')
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = gen_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ', ' + self.slug

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
