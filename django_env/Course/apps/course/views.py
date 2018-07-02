# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    course = Course.objects.all()
    context = {
        "course":course
    }
    return render(request, 'course/index.html', context)

def create(request):
    Course.objects.create(
        name=request.POST["name"],
        desc=request.POST["desc"]
    )
    return redirect('/')

def show(request, course_id):
    current_course = Course.objects.get(id=course_id)
    context = {
        "course":current_course
    }
    return render(request, "course/show.html", context)

def delete(request,id):
    current_course = Course.objects.get(id=id)
    return redirect(request, 'course/delete.html')

