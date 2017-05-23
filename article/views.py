#-*- coding: utf-8 -*-
from time import timezone

from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from article.forms import CommentForm
from article.models import Article, Comment
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.middleware.csrf import _get_new_csrf_token, rotate_token



def articles(request):
    return render(request,
                  'article/single.html',
                  {'articles': Article.objects.all(), 'username': auth.get_user(request).username})


def login(request):
    args = {}
    args.update(csrf(request))
    args['username'] = request.user.username
    if request.POST:
        print request.POST
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponse('')
        else:
            args['login_error'] = "Ошибка авторизации"
            return render_to_response('article/index.html', args)
    else:
        return render_to_response('article/index.html', args)


def logout(request):
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    args['username'] = request.user.username
    if request.POST:
        print request.POST
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2']
            )
            auth.login(request, newuser)
            return redirect('/', args['username'])
        else:
            args['form'] = newuser_form
    return render_to_response('article/register.html', args)

def comments(request):
    args = {}
    comment_form = CommentForm
    args.update(csrf(request))
    args['comments'] = Comment.objects.all()
    args['form'] = comment_form
    args['username'] = request.user.username
    return render_to_response('article/comments.html', args)


def addcomment(request):
    args = {}
    args.update(csrf(request))
    args['username'] = request.user.username
    args['comments'] = Comment.objects.all()
    if request.POST and not request.user.is_anonymous:
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_anonymous():
                form.instance.comment_author = request.user
            form.save()
            args['form'] = form
            return HttpResponse('')
        return render_to_response('article/register.html', args)
    return redirect('/register/', {'username': request.user.username})

def about(request):
    return render_to_response('article/about.html')