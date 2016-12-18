__author__ = 'IFIYEMI'

from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^$',views.welcome,name='welcome'),
     url(r'^lists$',views.lists,name='lists'),
    url(r'^add$',views.create,name='create'),


]