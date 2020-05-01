import urllib.request,urllib.parse,urllib.error
import json
place_name = input("Enter a place name: ")
base_url = "http://py4e-data.dr-chuck.net/json?"
address_param = urllib.parse.urlencode({'address': place_name})
target = base_url + address_param
print("Retrieving {0}".format(target))
connection = urllib.request.urlopen(target)
data = connection.read().decode()
print("Retrieved ",len(data))
parsed_data = json.loads(data)
print("Place id", parsed_data["results"][0]["place_id"])