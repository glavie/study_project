from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^auth/login/', views.login, name='login'),
    url(r'^auth/logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^comments/', views.comments, name='comments'),
    url(r'^addcomment/$', views.addcomment, name='addcomment'),
    url(r'^about/$', views.about, name='about'),
]