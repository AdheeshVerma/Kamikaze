from django.http import JsonResponse,HttpResponse
from recommendation_service.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
def welcomeMsg(req):
        return HttpResponse("Welcome to reccomendation Engines")

@require_POST
@csrf_exempt
def add_new_user(req):
    try:
        raw_data = json.loads(req.body)
        print(raw_data)
        user = User(**raw_data).save()
        if not user:
            raise Exception("user addition error")
        return JsonResponse({"message":str(user)})
    except Exception as e:
        return JsonResponse({"message":str(e)})

    
def get_all_user(req):
    try:
        user = User.nodes.all()
        data = []
        for i in user:
            data.append(str(i))
        return JsonResponse({"message":data})
    except Exception as e:
        return JsonResponse({"message":str(e)})

@require_POST
@csrf_exempt
def get_user_by_id(req):
    try:
        raw_data = json.loads(req.body)
        username=raw_data['username']
        if not username:
            raise Exception("username is required")
        
        db_node = User.nodes.first_or_none(**raw_data)
        print(db_node)
        if not db_node:
            raise Exception("user not found")
        
        return JsonResponse({"message":str(db_node)})
    except Exception as e:
        print(e)
        return JsonResponse({"message":str(e)})
    
def get_user_anime(req):
    try:
        raw_data = json.loads(req.body)
        username=raw_data['username']
        if not username:
            raise Exception("username is required")
        
        db_nodes = User.nodes.get_or_none(**raw_data)
        if not db_nodes:
            raise Exception("user doesn't exists")
        
        # find all the animes that the user has watched
    except Exception as e:
        print(e)
        return JsonResponse({"message":str(e)})
    
def get_user_friends():
    try:
        pass
    except Exception as e:
        print(e)
        return JsonResponse({"message":str(e)})
def recommend_anime():
    try:
        pass
    except Exception as e:
        print(e)
        return JsonResponse({"message":str(e)})
def recommend_friends():
    try:
        pass
    except Exception as e:
        print(e)
        return JsonResponse({"message":str(e)})
