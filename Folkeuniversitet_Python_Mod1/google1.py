#https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search

import urllib.parse
import urllib.request
import simplejson

num_queries = 50*4
query = urllib.parse.urlencode({'q' : 'example'})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query

for start in range(0, num_queries, 4):
    request_url = '{0}&start={1}'.format(url, start)
    search_results = urllib.request.urlopen(request_url)
    json = simplejson.loads(search_results.read())
    print(json)
    results = json['responseData']['results']
    for i in results:
        print(i['title'] + ": " + i['url'])
