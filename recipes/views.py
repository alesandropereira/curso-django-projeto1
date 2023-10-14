from django.http import HttpResponse
from django.shortcuts import render

def v_home(request):
    return HttpResponse('home view return')

def v_about(request):
    return HttpResponse('about view return')

def v_contact(request):
    return HttpResponse('contact view return')