# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Carreras
from ..authentication.models import SimuladorUser

@login_required(login_url="/login/")
def index(request):
    sistemas = None

    user = SimuladorUser.objects.get(user=request.user)

    sistemas = Carreras.objects.get(codigo_carrera=user.carrera).nombre

    if sistemas is None: raise Exception("No está la carrera en la base de datos")

    context = {'segment': 'index', 'carrera': sistemas}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def planes(request):
    context = {}
    html_template = loader.get_template('home/planes.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def competencias(request):
    context = {}
    html_template = loader.get_template('home/competencias.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def asignaturas(request):
    context = {}
    html_template = loader.get_template('home/asignaturas.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def titulos(request):
    context = {}
    html_template = loader.get_template('home/titulos.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def optativas(request):
    context = {}
    html_template = loader.get_template('home/optativas.html')
    return HttpResponse(html_template.render(context, request))

