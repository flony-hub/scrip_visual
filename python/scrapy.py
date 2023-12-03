
import requests
from bs4 import BeautifulSoup
from lxlm import *
 
url = "https://www.wikipedia.org/"
encabezado = {
    "user-agent":"Mozila/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML like Gecko) Ubuntu Chromiun/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }
respuesta = requests.get(url, headers=encabezado)

parser = html.fromstring(respuesta.text)
español = parser.get_elemet_by_id("js-link-box-es")
print (español.text_content())