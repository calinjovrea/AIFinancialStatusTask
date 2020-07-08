import scrapy


class AddressSpider(scrapy.Spider):
    name = "addressesofrestaurants"

    def start_requests(self):


        urls = [
            'https://tosseduk.com/locations/baker-street/',
            'https://www.gbk.co.uk/location/covent-garden?address',
            'https://www.superfishuk.co.uk/branches/ashtead/',
            'https://theivysohobrasserie.com/',
        ]
        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        regex_selectors_results = response.xpath('string(//*)').re(r"\d{1,2}\D\d+[ ]\w+[ ]\w+")
        
        return {'restaurant_street_address': regex_selectors_results[0]}