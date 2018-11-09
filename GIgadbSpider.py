from Spider import *
import xmltodict 


class GigadbSpider(Spider):
    def __init__(self, baseUrl, delay, fileName):
        super().__init__(baseUrl, delay, fileName)
    
    def crawl(self, maxDatasets):
        
        url = self.baseURL + "/dump"
        response = requests.get(url)
        xmltodict.parse(response.text)
        

