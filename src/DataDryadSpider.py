from Spider import *

class DataDryadSpider(Spider):
    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = "https://api.datacite.org"
        self.dataStore = 'DataDryad'

    def crawl(self, maxDatasets):

        curPage = 1
        datasetsPerPage = 100
        count = 0

        res = requests.get(self.baseURL + "/works?page[size]=" + str(datasetsPerPage) + "&page[number]=" + str(1) + "&data-center-id=dryad.dryad")
        maxPages = res.json()["meta"]["total-pages"] # Max Pages in DataStore

        while count < maxDatasets and curPage < maxPages:

            url = self.baseURL + "/works?page[size]=" + str(datasetsPerPage) + "&page[number]=" + str(curPage) + "&data-center-id=dryad.dryad"
            response = requests.get(url)
            jsonData = response.json()

            datasetList = jsonData["data"]
            maxPages = jsonData["meta"]["total-pages"]

            for dataset in datasetList:

                doi = dataset['attributes']['doi']
                datasetURL = dataset['attributes']['url']

                urlPartList = datasetURL.split('/')
                print(datasetURL)

                if( datasetURL != "http://datadryad.org/publicationBlackout" and urlPartList[-1].isdigit() == False):
                    metaData = self.extract_metadata(datasetURL)
                    count += 1
                    if(self.cacheDataset(metaData, doi, self.dataStore)):
                        print('Dryad New Dataset Added : Total :' + str(count) )
                    else:
                        print("\n\n No metadata present [DataDryad] : Total : " + str(count) + "\n\n")
                    time.sleep(self.delay)
                else:
                    print("Unpublished Dataset in Dryad " + datasetURL)

                if(count == maxDatasets):
                    break

            curPage += 1

        # Write cache to File
        self.writeCacheToFile()