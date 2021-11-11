# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('planes', views.planes, name='planes'),
    path('competencias', views.competencias, name='competencias'),
    path('asignaturas', views.asignaturas, name='asignaturas'),
    path('titulos', views.titulos, name='titulos'),
    path('optativas', views.optativas, name='optativas'),
    re_path(r'^.*', views.pages, name='pages')
]
