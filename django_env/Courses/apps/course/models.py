# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from..login.models import User
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name field must be 5 characters or more")
        if len(post_data['desc']) < 30:
            errors.append("Description field must be 30 characters or more")
        return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()