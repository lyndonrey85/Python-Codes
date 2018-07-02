# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class travelManager(models.Manager):
    def travel_validation(self, postData, id):
        errors=[]
        if len(postData['destination']) < 1 :
            errors.append("Destination field can not be empty")
        if len(postData['description']) < 1 :
            errors.append("Description field can not be empty")
        if str(date.today()) > str(postData['start']):
            errors.append("Please input a valid Date. Note: Start time can not be in the past.")
        if str(date.today()) > postData['end']:
            errors.append("Please input a valid Date. Note: End date must be in the future")
        if postData['start'] > postData['end']:
            errors.append("Travel Date From can not be in the future of Travel Date To")
        if len(errors) == 0:
            plan= Travel.objects.create(destination=postData['destination'],description=postData['description'], start=postData['start'],end=postData['end'], creator= User.objects.get(id=id))
            print "Successfully created new plan:"
            return (True, plan)
        else:
            print "Cannot input into Data"
            return (False, errors)

    def join(self, id, travel_id):
        if len(Travel.objects.filter(id=travel_id).filter(join__id=id))>0:
            return {'errors':'You already Joined this'}
        else:
            joiner= User.objects.get(id=id)
            plan= self.get(id= travel_id)
            plan.join.add(joiner)
            return {}


class Travel(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    start= models.DateField()
    end= models.DateField()
    creator= models.ForeignKey(User, related_name= "planner")
    join= models.ManyToManyField(User, related_name="joiner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = travelManager()
# class Travel(models.Model):
#     destination = models.CharField(max_length=100)
#     description = models.CharField(max_length=255)
#     start = model.DateField()
#     end = DateField()
#     creator = models.ForeignKey(User, related_name = "planner")
#     join = models.ManyToManyField(User, related_name = "joiner")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = travelManager()