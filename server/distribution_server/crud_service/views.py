from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import CustomUser as User
from .api_validater import RegisterModel, LoginModel
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import login

def welcomeMsg(req):
    return HttpResponse("Welcome to Crud Services")

@csrf_exempt
@require_POST
def register_user(req):
    try:
        if req.method=='POST':
            raw_data = json.loads(req.body)
            user_data = RegisterModel(**raw_data)
            
            db_user = User.objects.filter(email=user_data.email)
            if db_user:
                raise Exception("user already exist")

            check_username = User.objects.filter(username=user_data.username).exists()
            if(check_username):
                raise Exception("username already taken")
            
            created_user = User.objects.create(**raw_data)
            created_user.set_password(user_data.password)
            created_user.save()
            if not created_user:
                raise Exception("unable to create user")

            return JsonResponse({"message":"user created successfully","status":"success","code":"200"})
    except Exception as e:
        return JsonResponse({"message":str(e),"status":"failed","code":"400"})
    
@csrf_exempt
@require_POST
def login_user(req):
    try:
        raw_data = json.loads(req.body)
        user_data = LoginModel(**raw_data)
        # check if user exists
        db_user = User.objects.filter(email=user_data.email)
        db_user_exists = db_user.exists()
        if not db_user_exists:
            raise Exception('user not found. kindly register')
        
        # TODO: match the password
        print(user_data.password == db_user.Password)
        
        return JsonResponse({"data":{"token":"token_value"},"status":"success","code":"400"})
    except Exception as e:
         return JsonResponse({"message":str(e),"status":"failed","code":"400"})

def add_anime(req):
    pass