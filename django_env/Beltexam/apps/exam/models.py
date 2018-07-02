# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from..login.models import User
from django.db import models

# Create your models here.
class FriendManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name field must be 5 characters or more")
        return errors

class Friend(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    new_friend = models.CharField(max_length=100, default=1)
    creator = models.ForeignKey(User, related_name="friends_added", default=1)
    other_users = models.ManyToManyField(User, related_name="other_user")
    created_at = models.DateTimeField(auto_now_add=True)
