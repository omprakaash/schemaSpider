from Spider import *

class DataDryadSpider(Spider):
    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = "https://api.datacite.org"
        self.dataStore = 'DataDryad'

    def crawl(self, maxDatasets):

        curPage = 40
        datasetsPerPage = 100
        count = 0

        while count < maxDatasets:

            url = self.baseURL + "/works?page[size]=" + str(datasetsPerPage) + "&page[number]=" + str(curPage) + "&data-center-id=dryad.dryad&"
            response = requests.get(url)
            jsonData = response.json()

            datasetList = jsonData["data"]

            for dataset in datasetList:

                doi = dataset['attributes']['doi']
                datasetURL = dataset['attributes']['url']

                urlPartList = datasetURL.split('/')
                print(datasetURL)

                if( datasetURL != "http://datadryad.org/publicationBlackout" and urlPartList[-1].isdigit() == False):
                    metaData = self.extract_metadata(datasetURL)
                    if(self.cacheDataset(metaData, doi, self.dataStore)):
                        print('Dryad New Dataset Added : Total :' + str(count) )
                    else:
                        print("\n\n No metadata present [DataDryad] : Total : " + str(count) + "\n\n")
                    count += 1
                    time.sleep(self.delay)
                else:
                    print("Unpublished Dataset in Dryad " + datasetURL)

                if(count == maxDatasets):
                    break

            curPage += 1

        # Write cache to File
        self.writeCacheToFile()