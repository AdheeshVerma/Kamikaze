import requests
from django.http import HttpResponse
from .models import Genre

def populate_genres(req):
    ENDPOINT = "https://api.jikan.moe/v4/genres/anime"
    headers = {
        "Content-Type": "application/json",
    }
    
    try:
        response = requests.get(ENDPOINT, headers=headers)
        response.raise_for_status() 
        data = response.json()
        data=data["data"] 
        
        for i in data:
            genre = i["name"].lower()
            # add to the neo4j database if not exists
            db_check = Genre.nodes.get_or_none(genre=genre)
            if db_check:
                continue

            add_to_db = Genre(**{"genre":genre}).save()

        return HttpResponse("successful")
    except requests.exceptions.RequestException as e:
        return HttpResponse("not successful")

