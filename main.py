from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

PAGE = "MercadoLibre"


class Article(Item):
    title = Field()
    price = Field()
    units_sold = Field()
    url = Field()
    url_image = Field()


class Crawler(CrawlSpider):
    name = PAGE
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "CLOSESPIDER_PAGECOUNT": 5000 # Number of pages to scrap
    }

    download_delay = 1  # Tiempo que se demora en cada requerimiento

    allowed_domains = ["listado.mercadolibre.com.co", "articulo.mercadolibre.com.co"]

    start_urls = ["https://listado.mercadolibre.com.co/ropa/hoddie"]

    rules = (
        # Paginación
        Rule(
            LinkExtractor(
                allow=r"/hoddie_Desde_"
            ), follow=True
        ),
        # Detalle de los productos
        Rule(
            LinkExtractor(
                allow=r'/MCO-'
            ), follow=True, callback="parse_items"
        )
    )

    def parse_items(self, response):
        item = ItemLoader(Article(), response)
        item.add_xpath("title", "//h1/text()")
        # item.add_xpath("price", "//span[@class = 'price-tag-fraction']/text()")
        item.add_xpath("price", "//div[@class = 'ui-pdp-price mt-16 ui-pdp-price--size-large']//div[@class = 'andes-tooltip__trigger']//span[@class = 'price-tag-fraction']/text()")
        item.add_xpath("units_sold", "//div[@class='ui-pdp-header__subtitle']/span/text()")
        item.add_value("url", response.url)
        item.add_value("url_image", response.xpath("//div[@class = 'ui-pdp-container__row ui-pdp-container__row--gallery']//div[@class = 'ui-pdp-gallery']//div[@class = 'ui-pdp-gallery__column']//span[@class = 'ui-pdp-gallery__wrapper']//figure[@class = 'ui-pdp-gallery__figure']/img/@src").get())

        yield item.load_item()
