# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
# from ..login.models import Course
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect ("course:index")

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect ("course:index")

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def show(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.courses_left.all().values("course").distinct()
    unique_course = []
    for course in unique_ids:
        unique_course.append(course.objects.get(id=course['course']))
    context = {
        'user': user,
        'unique_course_desc': unique_desc
    }
    return render(request, 'users/show.html', context)
