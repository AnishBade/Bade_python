import requests_cache
#its not found in the permanent cache
res=requests_cache.get("https://api.datamuse.com/words?rel_rhy-happy",permanent_cache_file="datamuse_cache.txt")
#^this will check the cache first and if data not found in the cache, it performs
#normal get requests
print(res.text[:100])
#this time it will be found in the temporary cache
res=requests_cache.get("https://api.datamuse.com/words?rel_rhy=happy",permanent_cache_file="datamuse_cache.txt")
#this one is in the permanent cache.
res=requests_cache.get("https://api.datamuse.com/words?rel_rhy=funny",permanent_cache_file="datamuse_cache.txt")

