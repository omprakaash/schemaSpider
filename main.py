from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *
from ZenodoSpider import *

def main():
    delay = 15
    maxDatasets = 4
    baseURL = "https://zenodo.org/api"
    spider = ZenodoSpider(baseURL, delay, "ZenodoData.json")

    spider.crawl(maxDatasets)

if __name__ == '__main__':
    main()