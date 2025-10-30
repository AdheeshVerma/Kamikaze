from neomodel import StructuredNode, StringProperty,UniqueIdProperty, RelationshipTo,RelationshipFrom

class Genre(StructuredNode):
    genre = StringProperty(required=True)
    animes = RelationshipFrom('Anime', 'BELONGS_TO')

class Anime(StructuredNode):
    name = StringProperty(unique_index=True)
    genre = RelationshipTo('Genre', 'BELONGS_TO')
    watchers = RelationshipFrom('User', 'WATCHES')

class User(StructuredNode):
    uid = UniqueIdProperty()
    username = StringProperty(unique_index=True)

    anime = RelationshipTo('Anime', 'WATCHES')
    knows = RelationshipTo('User', 'KNOWS')
    known_by = RelationshipFrom('User', 'KNOWS')
