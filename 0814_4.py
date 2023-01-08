import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.youtube.com/"

response = requests.get(url)

html = bs(response.text,"html.parser")

thumbs = html.select("a yt-img-shadow img", limit=5)


i = 14
for thumb in thumbs:
    urlretrieve(thumb["src"], str(i)+".jpg")
    i += 1