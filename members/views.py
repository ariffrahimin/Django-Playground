from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader as LD

def members(request):
    template = LD.get_template('myfirst.html')
    return HttpResponse(template.render())