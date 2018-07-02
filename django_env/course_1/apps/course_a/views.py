# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from ..login.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    courses = Course.objects.all()
    current_user = User.objects.get(id=request.session["user_id"])
    user_favorites = current_user.favorites.all()
    # course_delete = Course.objects.all().delete()
    context = {
        "courses": courses,
        "favorites": user_favorites
        # "course_to_remove": course_remove
    }
    return render(request, 'course_a/index.html', context)

def create(request):
    # errors = Course.objects.validate(request.POST)
    # if errors:
    #     for error in errors:
    #         error(request, error)
    # else:
    #     Course.objects.create(
    #         name=request.POST['name'],
    #         desc=request.POST['desc']
    #     )
    current_user = User.objects.get(id=request.session["user_id"])
    new_courses = Course.objects.create(
        name=request.POST["name"],
        desc=request.POST["desc"],
        creator=current_user)
    return redirect("course_a:index")

def favorite(request, course_id):
    current_user = User.objects.get(id=request.session["user_id"])
    current_course = Course.objects.get(id=course_id)
    current_course.user_favorites.add(current_user)
    current_course.save()
    return redirect("course_a:index")

def show(request, course_id):
    current_course = Course.objects.get(id=course_id)
    context = {
        "course":current_course
    }
    return render(request, "course_a/show.html", context)

def destroy(request, course_id):
    # current_course = Course.objects.get(id=course_id)
    # current_user = User.objects.get(id=request.session["user_id"])
    # current_course.user_favorites.remove(current_user)
    # current_course.remove()
    # current_course.save()
    # return redirect("course_a:index")
   

    # course = Course.objects.all().remove()
    # course_name_to_remove = request.POST["name"]
    # course_desc_to_remove = request.POST["desc"]
    # course.name = course_name_to_remove
    # course.desc = course_desc_to_remove
    # course.remove()
    # return redirect("course_a:index")
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("course:index")


    
    # course = Course.objects.get(id = id)
    # course.remove()
    # return redirect("course_a:index")