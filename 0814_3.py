import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.google.com/search?q=cute+dog&rlz=1C5CHFA_enKR1018KR1018&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj9p5iN6sX5AhVQVN4KHRzFB3wQ_AUoAXoECAEQAw&biw=1440&bih=764&dpr=2"

response = requests.get(url)

html = bs(response.text,"html.parser")

thumbs = html.select("a div img", limit=10)


i = 5
for thumb in thumbs:
    urlretrieve(thumb["src"], str(i)+".jpg")
    i += 1
