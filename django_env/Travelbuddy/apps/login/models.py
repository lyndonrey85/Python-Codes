# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(username=post_data['username'])) > 0:
            # check this user's password
            user = self.filter(username=post_data['username'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('username/password incorrect')
        else:
            errors.append('username/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("name fields must be at least 3 characters")
        if len(post_data['username']) < 2:
            errors.append("usernamefields must be at least 3 characters")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")           
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('name fields must be letter characters only')
        # if not re.match(EMAIL_REGEX, post_data['email']):
        #     errors.append("invalid email")
        # if len(User.objects.filter(email=post_data['email'])) > 0:
        #     errors.append("email already in nameuse")
        if post_data['password'] != post_data['password_confirm']:
            errors.append("passwords do not match")

        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=post_data['name'],
                username=post_data['username'],
                # email=post_data['email'],
                password=hashed
            )
            return new_user
        return errors


class User(models.Model):
    name = models.CharField(max_length=100)
    # alias = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __str__(self):
        return self.username
