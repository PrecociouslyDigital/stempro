from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

# users/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add additional fields in here
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    type = models.CharField(max_length=50, blank=True)
    related_account = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email


class Course(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=200, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.neme

class SubscribeEmail(models.Model):
    subscribe_email = models.CharField(unique=True, max_length=200)
    create_date = models.DateField(default=date.today)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.subscribe_email

    def get_absolute_url(self):
        return reverse("subscribe_result", kwargs={})

class TutorActive(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=200, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50)

    def __str__(self):
      return self.name

class InvolvedActive(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=200, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50)

    def __str__(self):
      return self.name

class Program(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=200, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50)

    def __str__(self):
      return self.name


class RegisterActive(models.Model):
    active_name = models.CharField(max_length=200)
    who_register = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    register_date = models.DateField(default=date.today)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.who_register

    def get_absolute_url(self):
        return reverse("subscribe_result", kwargs={})
