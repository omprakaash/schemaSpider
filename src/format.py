import ndjson as nj
import json
import sys


# Script to format the data to match ElasticSearch BULk API input specification 
def main():

    inputfile = sys.argv[1]
    outputFile = sys.argv[2]

    with open(inputfile) as src:
        data = json.load(src)

    datasets = []

    for row in data:
        
        tempIdDict = dict()
        tempIdDict["index"] = { '_id' : row}

        datasets.append(tempIdDict)
        datasets.append(data[row])
    
    with open(outputFile,'w') as out:
        json.dump(datasets, out)

if __name__=='__main__':
    main()
