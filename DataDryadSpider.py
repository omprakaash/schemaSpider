from Spider import *

class DataDryadSpider(Spider):
    def __init__(self, baseUrl, delay, fileName):
        super().__init__(baseUrl, delay, fileName)

    def crawl(self, maxDatasets):

        curPage = 1
        datasetsPerPage = 2
        count = 0

        while count < maxDatasets:

            url = self.baseURL + "/works?page[size]=" + str(datasetsPerPage) + "&page[number]=" + str(curPage) + "&data-center-id=dryad.dryad"
            response = requests.get(url)
            jsonData = response.json()

            datasetList = jsonData["data"]

            for dataset in datasetList:
                datasetURL = dataset['attributes']['url']
                metaData = self.extract_metadata(datasetURL)

                if(self.cacheDataset(metaData)):
                    count += 1
                    pp.pprint(metaData)
                else:
                    print("\n\nSkipping Dataset - No metadata present\n\n")
            
                if(count == maxDatasets):
                    break

                time.sleep(self.delay)

            curPage += 1

        # Write cache to File
        self.writeCacheToFile()