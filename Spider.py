import os

import requests
import extruct
import time
import pprint
import json

from w3lib.html import get_base_url

pp = pprint.PrettyPrinter(indent=2)

class Spider:

    def __init__(self, baseUrl, delay):
        self.baseURL = baseUrl
        self.delay = delay
        self.datasets = dict()

    def extract_metadata(self, url):
        r = requests.get(url)
        base_url = get_base_url(r.text, r.url)
        data = extruct.extract(r.text.encode('utf8'), base_url=base_url)
        #print( data['json-ld'][0]['identifier'] )
        return(data)

    def crawl(self, max_pages):
        pass
    
    def writeToFile(self, fileName):
        with open(fileName, "w") as writeFile:
            json.dump(self.datasets, writeFile)
    




    


