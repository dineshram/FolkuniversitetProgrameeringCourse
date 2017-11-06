# https://github.com/richardasaurus/imdb-pie

from imdbpie import Imdb

imdb = Imdb()
imdb = Imdb(anonymize=True)

print(imdb.search_for_title("The Dark Knight"))
print()
print(imdb.search_for_person("Christian Bale"))
print()
print(imdb.get_episodes('tt0096697'))

top250 = imdb.top_250()

for i in range(0, len(top250)):
    print(top250[i])
    print()

title = imdb.get_title_by_id("tt1210166")
for person in title.credits:
    # check if they are a writer
    if person.token == 'writers':
        print(person.name + ' is a writer')
    else:
        print(person.name + ' is not a writer')
