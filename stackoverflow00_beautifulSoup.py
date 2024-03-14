import requests
from bs4  import BeautifulSoup

#Extracción de titulos y descripciones de la pg StackOverflow, utilizando Requests y Beatifull Soup

#USER AGENT PARA PROTEGERNOS DE BANEOS
encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebkit/537.36 (KHTML, LIKE Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36"
}
#URL SEMILLA
url ="https://stackoverflow.com/questions"

#REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url,headers=encabezado)
print(respuesta)
#print(respuesta.text)

#PARSEO DEL ARBOL CON BEATIFULL SOUP
soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary")

for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find('div', class_="s-post-summary--content-excerpt").text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r','') #LIMPIEZA DE TEXTO
    print(texto_pregunta)
    print(descripcion_pregunta)

#La pag se actualiza constantemente, por lo que traemos cambia. Si quisiera comparar con una pg web abierta lo que trae, deberia actualizarla al mismo tiempo que traigo la info. 