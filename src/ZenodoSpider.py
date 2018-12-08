from Spider import *

class ZenodoSpider(Spider):
    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = "https://zenodo.org/api"
        self.dataStore = 'Zenodo'

    def crawl(self, maxDatasets):

        count = 0
        curPage = 1
        datasetsPerPage = 20

        super().loadDataFromFile()

        while(count < maxDatasets):

            url = self.baseURL + "/records/?size=" + str(datasetsPerPage) + "&page=" + str(curPage) + "&type=dataset"
            response = requests.get(url)
            jsonData = response.json()

            if "status" in jsonData and jsonData["status"] == 400: # All datasets in database already read
                print("Max Reached")
                break

            datasetList = jsonData['hits']['hits']

            for dataset in datasetList:
                datasetURL = dataset['links']['html']
                doi = dataset['doi']
                metaData = self.extract_metadata(datasetURL)

                #pp.pprint(metaData)
                
                if(self.cacheDataset(metaData, doi, self.dataStore)):
                    count += 1
                    print("Zenodo: " + str(count))
                else:
                    print("\n\n No metadata present [ Zenodo ] for: " + doi+  "\n\n")
            
                if(count == maxDatasets):
                    break

                time.sleep(self.delay)
            
            curPage += 1

        # Write cache to File
        self.writeCacheToFile()
       


        

        