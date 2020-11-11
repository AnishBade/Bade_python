import requests
import json
page=requests.get("http://api.datamuse.com/words?rel_rhy=funny")
print(type(page))

print(page.text[:150]) #print the first 150 characters
print(type(page.text))
print(page.url)#print the url that was fetched
print("-------")
x=page.json() #turn page.text into a python object
#short form of json.loads(page.text)
print(x)
print(type(x))
print("------first item in the list-----")
print(x[0])
print("-----the whole list,pretty printed----")
print(json.dumps(x,indent=2))#pretty print the results
print(type(json.dumps(x,indent=2)))
