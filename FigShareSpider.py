from Spider import *

class FigShareSpider(Spider):
    def __init__(self, baseUrl, delay,  fileName):
        super().__init__(baseUrl, delay, fileName)
           
    def crawl(self, maxDatasets):
        # setting up tracking variables
        rowsPerPage = 10
        curCount = 0
        curPage = 1

        # Loading already scaped dataset dictonary from json file
        self.loadDataFromFile()

        while curCount < maxDatasets:

            url = self.baseURL + "/articles" + "?page=" + str(curPage) + "&page_size=" + str(rowsPerPage) + "&item_type=3"
            response = requests.get(url)
            jsonData = response.json()
            pp.pprint(jsonData)

            for dataSet in jsonData:
                # Each dataSet is a dictionary 

                doi = dataSet['doi']
                dataSetUrl = dataSet['url_public_html']
                metaData = super().extract_metadata(dataSetUrl)    
                self.datasets[doi] = metaData['json-ld'][0]

                curCount += 1
                if(curCount == maxDatasets):
                    break

                time.sleep(self.delay)
            
            curPage += 1

        # Write to File
        self.writeCacheToFile()