import os

import requests
import extruct
import time
import pprint
import json

from w3lib.html import get_base_url

pp = pprint.PrettyPrinter(indent=2)

class Spider:

    def __init__(self, delay, fileName):
        self.delay = delay
        self.datasets = dict()
        self.fileName = fileName

    def extract_metadata(self, url):
        r = requests.get(url)
        base_url = get_base_url(r.text, r.url)
        data = extruct.extract(r.text.encode('utf8'), base_url=base_url)
        return(data)

    def crawl(self, max_pages):
        pass
    
    def loadDataFromFile(self):
         # Loading already scaped dataset dictonary from json file
        try:
            with open(self.fileName) as data_file:
                try:
                    self.datasets = json.load(data_file)
                except ValueError:
                    self.datasets = dict()
        except FileNotFoundError:
            self.datasets = dict()

    def cacheDataset(self, metaData, doi, dataStore):
        if(len(metaData['json-ld']) > 0):
            metaData['json-ld'][0]['dataStore'] = dataStore
            metaData['json-ld'][0]['hasMetadata'] = True
            self.datasets[metaData['json-ld'][0]['@id']] = metaData['json-ld'][0]
            return True
        else:
            tempDict = dict()
            tempDict['hasMetadata'] = False
            tempDict['dataStore'] = dataStore
            self.datasets[doi] = tempDict
            return False

    def writeCacheToFile(self):
        with open(self.fileName, "w") as writeFile:
            json.dump(self.datasets, writeFile, ensure_ascii=False)
    




    


