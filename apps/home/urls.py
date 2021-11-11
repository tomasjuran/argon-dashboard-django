# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import re_path
from apps.home import views

urlpatterns = [
    re_path(r'^.*', views.pages, name='pages'),
]
