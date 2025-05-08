from film import MovieCatalog

#inizializzare un catalogo, ovvero un oggetto della classe moviecatalof

catalog:MovieCatalog=MovieCatalog()
# print(catalog.setCatalog())
# print(catalog)

catalog.add_movies("Steven Spielberg",["Casper","Ritorno al futuro"])
# print(catalog)
catalog.add_movies("Steven Spielberg",["ET"])
# print(catalog)
catalog.add_movies("Quentin Tarantino",["Pulp Fiction","Kill Bill"])
# print(catalog)
catalog.remove_movie("Quentin Tarantino","Kill Bill")
# print(catalog)
catalog.remove_movie("Quentin Tarantino","Pulp Fiction")
# print(catalog)
# print(catalog.list_directors())
print(catalog.get_movies_by_director("Tim Burton"))
print(catalog.get_movies_by_director("Steven Spielberg"))