import requests
#Acceso a wikipedia
encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebkit/537.36 (KHTML, LIKE Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36"
}

url ="https://www.wikipedia.org/"

respuesta = requests.get(url,headers=encabezado)

print(respuesta)
print(respuesta.text)