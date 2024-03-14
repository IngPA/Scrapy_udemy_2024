from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import   ItemLoader
from bs4  import BeautifulSoup

class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()

class StackOverflowSpider(Spider):
    name = "miPrimerSpider"
    custom_settings = {
    "user-agent": "Mozilla/5.0 (X11; Linuxx86_64) AppleWebkit/537.36 (KHTML, LIKE Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36"
    }
    start_urls = ["https://stackoverflow.com/questions"]

    def parse(self, response): 
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="s-post-summary--content"]')
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', './/div[@class="s-post-summary--content-excerpt"]/text()')

            yield item.load_item()

#Para correr este codigo utilizo comandos en la terminal: 
#scrapy runspider stackoverflow01_scrapy.py -O resultados.json:json
#scrapy: Es el comando principal de Scrapy que se utiliza para ejecutar arañas y otras funciones relacionadas con Scrapy.

#runspider: Es una subcomando de Scrapy que se utiliza para ejecutar una araña sin necesidad de tener un proyecto Scrapy completo. Esto significa que puedes ejecutar una araña individual sin necesidad de crear un proyecto Scrapy completo.

#archivo.py: Es el nombre del archivo Python que contiene la definición de tu araña.

#-O resultados.json: Es una opción de la línea de comando que especifica el nombre del archivo de salida donde se guardarán los datos extraídos. En este caso, el nombre del archivo de salida es resultados.json. La opción -O indica que Scrapy debe guardar los resultados en un archivo en lugar de imprimirlos en la consola.

#:json: Es otra opción de la línea de comando que especifica el formato de salida de los datos extraídos. En este caso, se especifica que los datos deben ser guardados en formato JSON.
            
#el O es de ouput, el :json indica el formato de salida
#La pag se actualiza constantemente, por lo que traemos cambia. Si quisiera comparar con una pg web abierta lo que trae, deberia actualizarla al mismo tiempo que traigo la info. 