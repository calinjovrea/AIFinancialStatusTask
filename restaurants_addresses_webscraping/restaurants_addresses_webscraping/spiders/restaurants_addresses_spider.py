import scrapy
import w3lib.html

class AddressSpider(scrapy.Spider):
    name = "addressesofrestaurants"

    def start_requests(self):


        urls = [
            'https://tosseduk.com/locations/baker-street/',
            'https://www.gbk.co.uk/location/covent-garden?address',
            'https://www.superfishuk.co.uk/branches/ashtead/',
            'https://theivysohobrasserie.com/',
        ]
        
        addresses_of_restaurants_dict = {}
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'addresses_of_restaurants': addresses_of_restaurants_dict}, headers=headers)

    def parse(self, response):
        
        if 'tosseduk' in response.url:
            tosseduk_address = self.tosseduk(response)
        
        if 'gbk' in response.url:
            gbk_address = self.gbk(response)

        if 'superfishuk' in response.url:
            superfishuk_address = self.superfishuk(response)

        if 'ivysohobrasserie' in response.url:
            ivysohobrasserie_address = self.ivysohobrasserie(response)

        if len(response.meta['addresses_of_restaurants'].items()) == 4:
            return response.meta['addresses_of_restaurants']

    def tosseduk(self, response):

        tosseduk_address = response.css('p.adr span::text').extract()
        
        response.meta['addresses_of_restaurants']['tosseduk'] = ', '.join([list_item for list_item in tosseduk_address])

        return response.meta['addresses_of_restaurants']['tosseduk']
    
    def gbk(self, response):

        gbk_address = response.css('div.location-address p::text').extract()

        response.meta['addresses_of_restaurants']['gbk'] = gbk_address[0]

        return response.meta['addresses_of_restaurants']['gbk']

    def superfishuk(self, response):

        superfishuk_address = response.css('div.gdlr-item.gdlr-content-item p::text').extract()
        
        response.meta['addresses_of_restaurants']['superfishuk'] = ', '.join([list_item.strip(' ') for list_item in superfishuk_address[1:5]])

        return response.meta['addresses_of_restaurants']['superfishuk'] 

    def ivysohobrasserie(self, response):

        ivysohobrasserie_address = response.css('div.landing-contact__address::text').extract()

        response.meta['addresses_of_restaurants']['ivysohobrasserie'] = ' '.join([list_item.strip() for list_item in ivysohobrasserie_address[1:3]])
        
        return response.meta['addresses_of_restaurants']['ivysohobrasserie'] 