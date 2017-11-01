#coding: utf-8
from imdb import IMDb
imdb_api = IMDb()

the_matrix = imdb_api.get_movie('0133093')
print(the_matrix['director'])

for person in imdb_api.search_person('Mel Gibson'):
        print(person.personID, person['name'])
