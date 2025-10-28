from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcomeMsg(req):
    return HttpResponse("Welcome to Crud Services")