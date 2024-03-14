import requests
from lxml import html


#Extracción de una data que nos interesa
encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebkit/537.36 (KHTML, LIKE Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36"
}

url ="https://www.wikipedia.org/"

respuesta = requests.get(url,headers=encabezado)

print(respuesta)
#print(respuesta.text)

parser = html.fromstring(respuesta.text)

#print(parser)

#espanol = parser.get_element_by_id("js-link-box-es")
#print(espanol.text_content())

espanol = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(espanol)