# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from .models import Carreras, Planes
from ..authentication.models import SimuladorUser

@login_required(login_url="/login/")
def planes(request):
    return default_response('planes', {}, request)

@login_required(login_url="/login/")
def competencias(request):
    return default_response('competencias', {}, request)

@login_required(login_url="/login/")
def asignaturas(request):
    return default_response('asignaturas', {}, request)

@login_required(login_url="/login/")
def titulos(request):
    return default_response('titulos', {}, request)

@login_required(login_url="/login/")
def optativas(request):
    return default_response('optativas', {}, request)

def default_response(segment, context, request):
    context = {**context, **getGlobalContext(request)}
    html_template = loader.get_template('home/' + segment + '.html')
    context['segment'] = segment
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = getGlobalContext(request)
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == '':
            load_template = 'index'

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template + '.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def getGlobalContext(request) -> dict:
    context = {}
    try:
        user = SimuladorUser.objects.get(user=request.user)
        carrera = Carreras.objects.get(codigo_carrera=user.carrera)
        context['carrera'] = carrera
        planes_list = Planes.objects.filter(codigo_carrera=carrera.codigo_carrera)
        context['planes_list'] = planes_list
    except ObjectDoesNotExist:
        pass
    return context