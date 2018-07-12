# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static


def hello(request):
    context = {}
    context['bars'] = "hello ~"
    return render(request, 'hello.html', context)