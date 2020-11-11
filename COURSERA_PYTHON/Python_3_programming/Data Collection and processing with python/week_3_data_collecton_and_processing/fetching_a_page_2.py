import requests
#page=requests.get("https://api.datamusecom/words?rel_rhy=funny")
kval_pairs={"rel_rhy":"funny"}
page=requests.get("https://api.datamuse.com/words",params=kval_pairs)
print(page.text[:150])#print the first 150 characters
print(type(page))
print(type(page.text))
print(page.url)#print the url that was fetched