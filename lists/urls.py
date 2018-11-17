"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lists import views
from . import views

urlpatterns = [
    #url(r'^new$', views.new_list, name='new_list'),
    url(r'^new$', views.new_Inst, name='new_Inst'),
    url(r'^(\d+)/$', views.view_inst, name='view_inst'),
    url(r'^(\d+)/add_item$', views.add_inst, name='add_inst'),

    #add Personal Education Objectives
    url(r'^1/inst/(\d+)', views.add_peos, name='add_peos'),
    url(r'^1/inst/(\d+)/newPeos/$', views.new_peos, name='new_peos'),
    #Add Student Outcomes.
    
    url(r'^1/inst/newSo/(\d+)', views.add_so, name='add_so'),
    url(r'^1/inst/newSo/(\d+)/newSo$', views.add_so, name='new_so'),
]