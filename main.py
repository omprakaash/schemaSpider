from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *
from ZenodoSpider import *
from DataDryadSpider import *

def main():
    delay = 15
    maxDatasets = 4
    baseURL = "https://api.datacite.org"
    spider = DataDryadSpider(baseURL, delay, "DryadData.json")

    spider.crawl(maxDatasets)

if __name__ == '__main__':
    main()