# Neo4j

Neo4j is the world’s leading Graph Database. It is a high performance graph store with all the features expected of a mature and robust database, like a friendly query language and ACID transactions. The programmer works with a flexible network structure of nodes and relationships rather than static tables — yet enjoys all the benefits of enterprise-quality database. For many applications, Neo4j offers orders of magnitude performance benefits compared to relational DBs.

## Setting up neo4j

so neo4j can be setup via 2 different ways one of them is the cloud native way i.e. you use a cloud provider to give you the information that you need and secondly use use a docker compose file to self host your own graph database.
in this project during development cycle we used a docker compose method to setup our own graph database.

Inorder to help us with graph database related things in django, we use `Django_neomodel`
`Django_neomodel` - a module that allows you to use the neo4j graph database with Django using neomodel.

I followed this [article](https://medium.com/swlh/create-rest-api-with-django-and-neo4j-database-using-django-nemodel-1290da717df9) inorder to setup the project.

Inorder to shape the migrations to the databse, use the following command

```bash
python3 manage.py install_labels
```

---

## Writing cypher queries
