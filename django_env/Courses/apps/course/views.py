# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import course
# from ..users.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "course": course.objects.all()
    }
    return render(request, 'course/index.html', context)

def create(request):
    errors = course.objects.validate(request.POST)
    if errors:
        for error in errors:
            error(request, error)
    else:
        course.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect('/course/create')

def confirm(request, course_id):
    context = {
        "course": course.objects.get(id=courses_id)
    }
    return render(request, 'course/index', context)

def delete(request, course_id):
    course.objects.get(id=course_id).delete()
    return redirect('/course/create')


