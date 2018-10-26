from HarvardSpider import *

def main():
    delay = 25
    maxDatasets = 1
    baseURL = "https://dataverse.harvard.edu"
    spider = HarvardSpider(baseURL, delay, "data.json")

    spider.crawl(maxDatasets)

if __name__ == '__main__':
    main()