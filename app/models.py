from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

# users/models.py
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    name = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    capacity = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # add additional fields in here
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    type = models.CharField(max_length=50, blank=True)
    related_account = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.email

class SignupProject(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=200)
    phone_number = models.CharField(max_length=50, null=True)
    school_name = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("subscribe_result", kwargs={})

class Course(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=3000, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

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
    summary = models.TextField(max_length=3000, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return self.name

class InvolvedActive(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=3000, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return self.name

class Program(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=3000, blank=True)
    regular_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    member_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True)
    adv_pic = models.ImageField(upload_to='profile_pics', blank=True)
    instructor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
      return self.name


class RegisterActive(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    active_name = models.CharField(max_length=200)
    who_register = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    register_date = models.DateField(default=date.today)
    is_paid = models.BooleanField(default=False)
    

    def __str__(self):
        return self.who_register

    def get_absolute_url(self):
        return reverse("subscribe_result", kwargs={})


class SignupEvent(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    event_name = models.CharField(max_length=200)
    number = models.IntegerField(default=1)
    register_date = models.DateField(default=date.today)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.who_register

    def get_absolute_url(self):
        return reverse("events", kwargs={})    


class SubscribePresentation(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=200)
    cellphone = models.CharField(max_length=50)
    grade = models.IntegerField()
    wechat = models.CharField(max_length=200, blank=True, null=True)
    schoolName = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subscribe_result", kwargs={})
