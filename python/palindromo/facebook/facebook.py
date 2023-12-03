import requests 
from bs4 import BeautifulSoup 

headers= {"user-agent":"Mozilla/5.0 (x11;Linux x86_64 AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromiun/71.0.3758.80 Chrome/71.0.3758.80 Safari/537.36)"}

url = 'https://stackoverflow.com/'

respuesta = requests.get(url, headers=headers)
 
soup= BeautifulSoup(respuesta.text, features="lxml")

contenedor_respuesta = soup.find(id="questions")
lista_de_preguntas = contenedor_respuesta.find_all('div', class_="s-post-summary")

for pregunta in lista_de_preguntas:
    descripcion_pregunta = pregunta.find('h3').text
    print(descripcion_pregunta)

