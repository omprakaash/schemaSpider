from Spider import *

class OmicsdiSpider(Spider):
    def __init__(self, baseUrl, delay, fileName):
        super().__init__(baseUrl, delay, fileName)
    
    
    def crawl(self, maxDatasets):
        
        curPage = 0
        count = 0
        datasetsPerPage = 20

         # Loading already scaped dataset dictonary from json file
        super().loadDataFromFile()

        while count < maxDatasets:

            url = self.baseURL + "/ws/dataset/search?start=" + str(curPage) + "&size=" + str(datasetsPerPage)

            response = requests.get(url)
            jsonData = response.json()

            datasetList = jsonData['datasets']

            for dataset in datasetList:
                datasetId = dataset['id']
                datasetUrl = self.baseURL + "/dataset/arrayexpress-repository/" + datasetId
                metaData = super().extract_metadata(datasetUrl)

                #adding dataset to hashMap
                if(super().cacheDataset(metaData)):
                    pp.pprint(metaData)
                    count += 1
                else:
                    print("Skipping Dataset due to format error in Metadata/Metadata not present")

                if(count == maxDatasets):
                    break
                
                time.sleep(self.delay)

            curPage += 1
        
        self.writeCacheToFile()

