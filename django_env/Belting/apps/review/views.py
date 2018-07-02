# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Review, Author, Book
from ..login.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
    }
    return render(request, 'review/index.html', context)

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'review/add.html', context)

def show(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'review/show.html', context)

def create(request):
    errs = Review.objects.validate_review(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
    # current_user = User.objects.get(id=request.session["user_id"])
    # new_review = Review.objects.create(
    #     book=request.POST,
    #     review=request.POST,
    #     reviewer=current_user)
    # return redirect("review:index")
    return redirect(reverse("review:index"))

def create_additional(request, book_id):
    the_book = Book.objects.get(id=book_id)
    new_book_data = {
        'title': the_book.title,
        'author': the_book.author.id,
        'rating': request.POST['rating'],
        'review': request.POST['review'],
        'new_author': ''
    }
    errs = Review.objects.validate_review(new_book_data)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        Review.objects.create_review(new_book_data, request.session['user_id'])
    return redirect('/review/' + book_id)

# def destroy(request, review_id):
#     current_user = User.objects.get(id=request.session["user_id"])
#     review = Review.objects.get(id=review_id)
#     current_review.review.delete(current_user)
#     review.delete()
#     return redirect("review:index")
    # errs = Review.objects.validate_review(request.POST)
    # if errs:
    #     for e in errs:
    #         messages.error(request, e)
    # else:
    #     book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
    #     return redirect("review:index")
