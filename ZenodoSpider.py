from Spider import *

class ZemodoSpider(Spider):
    def __init__(self, baseUrl, delay, fileName):
        super().__init__(baseUrl, delay)
        self.fileName = fileName
    
    def crawl(self, maxDatasets):

        curCount = 0
        start = 0
        curPage = 1
        datasetsPerPage = 20

        url = self.baseURL + "search?size=" + str(datasetsPerPage) + "&page=" + str(curPage)

        

        