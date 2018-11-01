from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *

def main():
    delay = 15
    maxDatasets = 20
    baseURL = "https://www.omicsdi.org"
    spider = OmicsdiSpider(baseURL, delay, "omsciData.json")

    spider.crawl(maxDatasets)

if __name__ == '__main__':
    main()