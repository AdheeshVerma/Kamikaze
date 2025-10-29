from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def welcomeMsg(req):
    return HttpResponse("Welcome to Crud Services")

# def register_user(req):
