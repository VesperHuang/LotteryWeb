# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static


def user_sign_in(request):
    context = {}
    context['context'] = ""
    url_htm = "user_sign_in.html"
    if request.POST:
        if(request.POST['user_name'] != ""):
            request.session['user_name'] = request.POST['user_name']
            
        context['context'] = "from user_sign_in"
        url_htm = "index.html"
        
    return render(request, url_htm,context)

def user_sign_out(request):
    context = {}
    context['context'] = "from user_sign_in"

    try:
        del request.session['user_name']
    except KeyError:
        pass

    return render(request, 'index.html',context)

def index(request):
    context = {}
    context['context'] = "hello ~"
    return render(request, 'index.html', context)