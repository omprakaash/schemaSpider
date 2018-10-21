from HarvardSpider import *

def main():
    delay = 25
    baseURL = "https://dataverse.harvard.edu"
    spider = HarvardSpider(baseURL, delay, "data.json")

    spider.crawl(1)

if __name__ == '__main__':
    main()