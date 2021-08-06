from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import datetime


class gender(Enum):
    Male = "Male"
    Female = "Female"


class activity(Enum):
    High = "High"
    Mid = "Mid"
    Low = "Low"


class month(Enum):
    January = "January"
    February = "February"
    March  = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September =  "September"
    October = "October"
    November = "November"
    December = "December"



class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=7, choices=[(tag.name, tag.value) for tag in gender],default=gender.Female)
    dob = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username


class detail(models.Model):
    person = models.ForeignKey(person , on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    height = models.CharField(max_length=5, blank=True)
    weight = models.CharField(max_length=5, blank=True)
    active = models.CharField(max_length=7, choices=[(tag.name, tag.value) for tag in activity],default=activity.Low)

    def __str__(self):
        return self.person.user.username


class food(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.CharField(max_length=15, blank=True)
    fats =  models.IntegerField(blank=True, default=0)
    proteins =  models.IntegerField(blank=True, default=0)
    calorie = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class cal_sum(models.Model):
    person = models.ForeignKey(person , on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    calorie = models.IntegerField(default=0)

    def __str__(self):
        return self.person.user.username
