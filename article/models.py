#-*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models



class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

class Comment(models.Model):
    comment_text = models.TextField(verbose_name='Ваш отзыв')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_author = models.ForeignKey('auth.User', blank=True, null=True)