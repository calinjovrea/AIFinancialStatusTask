import chompjs
import html
import json
import scrapy

from w3lib.html import remove_tags


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
            restaurant_id = 'tosseduk'
        
        if 'gbk' in response.url:
            restaurant_id = 'gbk'

        if 'superfishuk' in response.url:
            restaurant_id = 'superfishuk'

        if 'ivysohobrasserie' in response.url:
            restaurant_id = 'ivysohobrasserie'

        selectors = response.xpath("//*[text()[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'address')]]")
        
        if 'script' in selectors[0].root.tag:
            selectors_dict = chompjs.parse_js_object(selectors[0].get())
            if 'address' in selectors_dict.keys():
                if 'streetAddress' in selectors_dict['address'].keys():
                    response.meta['addresses_of_restaurants'][restaurant_id] = selectors_dict['address']['streetAddress']
            elif 'location' in selectors_dict.keys():
                if 'address' in selectors_dict['location'].keys():
                    response.meta['addresses_of_restaurants'][restaurant_id] = selectors_dict['location']['address']
        else:
            selector_items = response.css('.'+'.'.join([class_item for class_item in selectors[0].root.getparent().classes])).extract()
            cleaned_items = ' '.join([w for w in remove_tags(selector_items[-1]).split(' ')[1:4]])
            response.meta['addresses_of_restaurants'][restaurant_id] = html.unescape(cleaned_items)

        if len(response.meta['addresses_of_restaurants'].items()) == 4:
            return response.meta['addresses_of_restaurants']