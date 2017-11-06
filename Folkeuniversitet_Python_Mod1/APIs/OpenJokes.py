import json
import requests
import urllib.request

url = "https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_ten"
header = {'x-requested-with': 'XMLHttpRequest'}

mainPage = requests.get(url, headers = header)

print (mainPage.json())

req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

##parsing json
for item in cont['type']['setup']:
    counter += 1
    print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
    print("----")

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
print("Number of titles: ", counter)
