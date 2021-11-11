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
def pages(request):
    context = {}
    try:
        user = SimuladorUser.objects.get(user=request.user)
        carrera = Carreras.objects.get(codigo_carrera=user.carrera)
        context['carrera'] = carrera
        planes = Planes.objects.filter(codigo_carrera=carrera.codigo_carrera)
        context['planes'] = planes
    except ObjectDoesNotExist:
        pass
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == '':
            load_template = 'index.html'

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

