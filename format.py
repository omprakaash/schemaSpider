import ndjson as nj
import json


# Script to format the data to match ElasticSearch BULk API input specification 
def main():

    with open('ZenodoData.json') as src:
        data = json.load(src)

    datasets = []

    for row in data:
        
        tempIdDict = dict()
        tempIdDict["index"] = { '_id' : row}

        datasets.append(tempIdDict)
        datasets.append(data[row])
    
    with open('out1.json','w') as out:
        json.dump(datasets, out)

if __name__=='__main__':
    main()
