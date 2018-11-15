from Spider import *

class HarvardSpider(Spider):

    def __init__(self, delay, fileName):
        super().__init__(delay, fileName)
        self.baseURL = "https://dataverse.harvard.edu"
        self.dataStore = 'Harvard'

    def crawl(self, maxDatasets):

        # setting up tracking variables
        rows = 10
        curCount = 0
        start = 0
        
        # Loading already scaped dataset dictonary from json file
        self.loadDataFromFile()

        while curCount < maxDatasets:

            url = self.baseURL + '/api/search?q=*&fq=metadataSource:"Harvard Dataverse"' + '&type=dataset' + "&start="  + str(start) 
            response = requests.get(url)
            data = response.json()
            #pp.pprint(data)
           
            # Reading in all datasets from one response(MAX : 10 )
            for row in data['data']['items']:

                print("In Inner Loop"+ "\n\n")

                dataset_url = row['url']
                doi = row['global_id']
                meta_data = super().extract_metadata(dataset_url)
                
                #adding dataset to hashMap
                if(self.cacheDataset(meta_data, doi, self.dataStore)):
                    #pp.pprint(meta_data)
                    pass
                else:
                    print("No metadata present [ Harvard ] ")
        
                if(curCount == maxDatasets):
                    break

                # Crawler delay
                time.sleep(self.delay)

                curCount += 1
                print("Harvard: " + str(curCount) )

            # Page offset
            start += rows
            #print(start)

         # Write to File
        self.writeCacheToFile()

    def cacheDataset(self, metaData, doi, dataStore):
        if(len(metaData['json-ld']) > 0):
            metaData['json-ld'][0]['dataStore'] = dataStore
            metaData['json-ld'][0]['hasMetadata'] = True
            self.datasets[metaData['json-ld'][0]['identifier']] = metaData['json-ld'][0]
            return True
        else:
            tempDict = dict()
            tempDict['hasMetadata'] = False
            tempDict['dataStore'] = dataStore
            self.datasets[doi] = tempDict
            return False