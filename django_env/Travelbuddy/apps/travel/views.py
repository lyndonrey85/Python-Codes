from __future__ import unicode_literals
from .models import Travel
from ..login.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def index(request):
    return render(request, 'travel/index.html')

def travel(request):
    if 'id' not in request.session:
        return redirect ("/")
    context = {
        "user": User.objects.get(id=request.session['id']),
        "travels" : Travel.objects.all(),
        "others": Travel.objects.all().exclude(join__id=request.session['id'])
    }
    return render(request, 'travel/index.html', context)


def addplan(request):
    if 'id' not in request.session:
        return redirect ("/")
    else:
        context= {
            "user":User.objects.get(id=request.session['id']),
        }
        return render(request, 'travel/add.html', context)
    # if request.method != 'POST':
    #     return redirect ("/addplan")
    # newplan= Travel.objects.travel_validation(request.POST, request.session["id"])
    # if newplan[0] == True:
    #     return redirect('/travel')
    # else:
    #     for message in newplan[1]:
    #         messages.error(request, message)
    #     return redirect('/add')

def create(request):
    if request.method != 'POST':
        return redirect ("/index")
    newplan= Travel.objects.travel_validation(request.POST, request.session["id"])
    if newplan[0] == True:
        return redirect('/travel/index')
    else:
        for message in newplan[1]:
            messages.error(request, message)
        return redirect('/travel')

def show(request, travel_id):
    try:
        travel= Travel.objects.get(id=travel_id)
    except Travel.DoesNotExist:
        messages.info(request,"Travel Not Found")
        return redirect('/travel')
    context={
        "travel": travel,
        "user":User.objects.get(id=request.session['id']),
        "others": User.objects.filter(joiner__id=travel.id).exclude(id=travel.creator.id),
    }
    return render(request, '/travel/show.html', context)

def join(request, travel_id):
    if request.method == "GET":
        messages.error(request,"What trip?")
        return redirect('/travel')
    joiner= Travel.objects.join(request.session["id"], travel_id)
    print 80 * ('*'), joiner
    if 'errors' in joiner:
        messages.error(request, joiner['errors'])
    return redirect('travel:index')

def delete(request, id):
    try:
        target= Travel.objects.get(id=id)
    except Travel.DoesNotExist:
        messages.info(request,"Message Not Found")
        return redirect('/travel')
    target.delete()
    return redirect('/travel')

def logout(request):
    request.session.clear()
    return redirect('/')