#recommedation

import json
import urllib.parse

url_start = '<iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q='
url_address = '651%20E%20Peltason%20Dr%2C%20Irvine%2C%20CA%2092617%2C%20USA'
url_api_key = '&key=AIzaSyDtGrFbcJ8VzRCMXOQZICg-jReGRGEhmGE" allowfullscreen></iframe>'

data = json.load(open('locIndex.json'))

for k in data:
    print(data[k])

locs = sorted(data, key=lambda i: data[i].get('avg_hr'))

print('---------')
print()
for k in locs:
    s = url_start + urllib.parse.quote(data[k].get('name')) + url_api_key
    print(s)
