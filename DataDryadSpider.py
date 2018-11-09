from Spider import *

class DataDryadSpider(Spider):
    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = "https://api.datacite.org"

    def crawl(self, maxDatasets):

        curPage = 30
        datasetsPerPage = 10
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
                    print('Dryad New Dataset Added : Total :' + str(count) )
                else:
                    print("\n\nSkipping Dataset - No metadata present [DataDryad] : Total : " + str(count) + "\n\n")
            
                count += 1

                if(count == maxDatasets):
                    break

                time.sleep(self.delay)

            curPage += 1

        # Write cache to File
        self.writeCacheToFile()