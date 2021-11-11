# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path(r'^login.*', login_view, name="login"),
    path("logout", LogoutView.as_view(), name="logout")
]
