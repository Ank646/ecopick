# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.utils import timezone

User = get_user_model()


class userpro(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    username = models.TextField(blank=True)
    address = models.TextField(blank=True)
    fullname = models.TextField(blank=True)
    image = models.ImageField(upload_to='userproimg', default='profile.webp')
    password = models.TextField(blank=True)
    pincode = models.TextField(blank=True)
    isverified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=200, blank=True)


class picker(models.Model):
    name = models.TextField(blank=True)
    password = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    emaill = models.TextField(blank=True)
    image = models.ImageField(upload_to='proimg', default='profile.webp')
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    username = models.TextField(blank=True)


class dcenter(models.Model):
    name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    pincode = models.TextField(blank=True)
    about = models.TextField(blank=True)


class product(models.Model):
    name = models.TextField(blank=True)
    price = models.TextField(blank=True)
    image = models.ImageField(upload_to='productimg', default='profile.webp')
    detail = models.TextField(blank=True)


class order(models.Model):
    address = models.TextField(blank=True)
    quantity = models.TextField(blank=True)
    imgg = models.ImageField(upload_to='productimg', default='profile.webp')
    majority = models.TextField(blank=True)
    username = models.TextField(blank=True)
    weight = models.TextField(blank=True)
    message = models.TextField(blank=True)
    timee = models.DateTimeField(default=datetime.now)
    orderid = models.TextField(blank=True)
