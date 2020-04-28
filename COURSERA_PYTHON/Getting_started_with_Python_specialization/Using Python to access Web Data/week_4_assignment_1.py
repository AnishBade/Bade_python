import urllib.request
#we can also use alternative import method:
# from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total=0
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
#or html=urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    num=int(tag.text)
    total+=num
print(total)