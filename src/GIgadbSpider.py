from Spider import *
import xmltodict 


class GigadbSpider(Spider):
    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = ""
    
    def crawl(self, maxDatasets):
        
        url = self.baseURL + "/dump"
        response = requests.get(url)
        xmltodict.parse(response.text)
        

