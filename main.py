from HarvardSpider import *

def main():
    delay = 25
    baseURL = "https://dataverse.harvard.edu/dataverse/harvard?q=&fq0=metadataSource%3A%22Harvard+Dataverse%22&types=dataverses%3Adatasets&sort=dateSort&order=desc&page="
    spider = HarvardSpider(baseURL, delay)

    spider.crawl(2)

if __name__ == '__main__':
    main()