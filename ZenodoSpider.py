from Spider import *

class ZenodoSpider(Spider):
    def __init__(self, baseUrl, delay, fileName):
        super().__init__(baseUrl, delay, fileName)
    
    def crawl(self, maxDatasets):

        count = 0
        curPage = 1
        datasetsPerPage = 20

        super().loadDataFromFile()

        while(count < maxDatasets):

            url = self.baseURL + "/records/?size=" + str(datasetsPerPage) + "&page=" + str(curPage) + "&type=dataset"
            response = requests.get(url)
            jsonData = response.json()

            datasetList = jsonData['hits']['hits']

            for dataset in datasetList:
                datasetURL = dataset['links']['html']
                metaData = self.extract_metadata(datasetURL)

                if(self.cacheDataset(metaData)):
                    count += 1
                    pp.pprint(metaData)
                else:
                    print("\n\nSkipping Dataset - No metadata present\n\n")
            
                time.sleep(self.delay)
            
            curPage += 1

        # Write cache to File
        self.writeCacheToFile()
       


        

        