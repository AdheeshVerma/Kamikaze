from django.http import HttpResponse
from .models import Anime as AnimeModel
from recommendation_service.models import Anime, Genre
import requests
import time

'''
So what we are going to do is traverse over each page of the jikan api
and for each entry we are going to make a database storage in our sqlite db 
and our graph database. This might increase the first time db startup but eventually will not 
affect the server much

There are going to be 2 functions populate_db and populate_graph_db which populate the anime field
of both type of databases.

Now in populate_db it is just going to register the name and the jikan id while in 
populate_graph_db it is going to firstly add the node Anime and then define the relation of 
these with genre

now since the api has a limit of 60 request per minute we can make sure in one minutes we make
only 2 api calls 
'''


def populate_graph_db(name: str, genre: list[str]) -> bool:
    retry = True
    while retry:
        try:
            db_check = Anime.nodes.get_or_none(name=name.lower())
            if db_check:
                return True

            add_to_db = Anime(name=name.lower()).save()
            if not add_to_db:
                return False

            validate_genre = []
            for g in genre:
                db_genre = Genre.nodes.get_or_none(genre=g.lower())
                if db_genre:
                    validate_genre.append(db_genre)
                else:
                    created_genre = Genre(genre=g.lower()).save()
                    validate_genre.append(created_genre)

            for g in validate_genre:
                # g.anime.build_manager()
                add_to_db.genre.connect(g)

            retry = False
            return True
        except Exception as e:
            print(e)
            time.sleep(1000)
    return True


def populate_db(name: str, jikan_id: str) -> bool:
    retry = True
    while retry:
        try:
            db_check = AnimeModel.objects.filter(jikan_id=jikan_id, name=name)

            if db_check:
                return True

            add_to_db = AnimeModel(**{"jikan_id": jikan_id, "name": name}).save()
            if add_to_db:
                return True

            retry = False
            return True
        except Exception as e:
            print(e)
            time.sleep(1000)
    return True


def populate_api_data(req):
    PAGE = 1
    HAS_NEXT = True
    while HAS_NEXT:
        try:
            print(f"----------------PAGE={PAGE}---------------")
            ENDPOINT = f"https://api.jikan.moe/v4/anime?page={PAGE}"
            headers = {
                "Content-Type": "application/json",
            }
            response = requests.get(ENDPOINT, headers=headers)
            response.raise_for_status()
            data = response.json()

            HAS_NEXT = data["pagination"]["has_next_page"]

            for i in data["data"]:
                print(i["title"])
                db = populate_db(i["title"], i["mal_id"])
                if db:
                    print("Successfully saved in database")
                else:
                    print("Error saving in database")

                genres = [g["name"].lower() for g in i["genres"]]
                graph_db = populate_graph_db(i["title"], genres)
                if graph_db:
                    print("Saved to graph database")
                else:
                    print("Error saving in graph database")
            PAGE += 1

        except Exception as e:
            print(e)
            return HttpResponse(str(e))

    return HttpResponse("Data populated successfully")