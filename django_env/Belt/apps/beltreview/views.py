# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Review, Author, Book
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
    }
    return render(request, 'review/index.html', context)

