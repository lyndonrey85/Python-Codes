# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Friend
from ..login.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    friend = Friend.objects.all()
    # current_user.save()
    context = {
        "friend":friend
    }
    return render(request, 'exam/index.html', context)

def create(request):
    current_user = User.objects.get(id=request.session["user_id"])
    current_user.save()
    new_friend = Friend.objects.create(
        name=request.POST["name"],
        creator=current_user)
    return redirect("exam:index")

def show(request, friend_id):
    current_friend = Friend.objects.get(id=friend_id)
    context = {
        "friend":friend
    }
    return render(request, "exam/show.html", context)

def add(request, friend_id):
    current_user = User.objects.get(id=request.session["user_id"])
    current_user.save()
    new_friend = Friend.objects.add(
        name=request.POST["name"],
        creator=current_user)
    # return redirect("exam:index")
    return render(request, 'exam/index.html')

def view_profile(request, friend_id):
    current_friend = Friend.objects.get(id=friend_id)
    current_user = User.objects.get(id=request.session["user_id"])
    current_friend.save()
    other_user = Friend.objects.other_user(
        name=request.POST["name"],
        creator=current_user)
    return redirect("exam:index")

def delete(request, friend_id):
    friend_delete = Friend.objects.get(id=friend_id)
    current_user = User.objects.get(id=request.session['user_id'])
    friend_delete.delete()
    return redirect("exam:index") 
