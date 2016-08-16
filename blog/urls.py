'''
Created on 16 ago. 2016

@author: antonio
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
               url(r'^$', views.post_list),
               ]