# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('planes', views.planes),
    path('competencias', views.competencias),
    path('asignaturas', views.asignaturas),
    path('titulos', views.titulos),
    path('optativas', views.optativas),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
