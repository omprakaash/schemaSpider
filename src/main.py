from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *
from ZenodoSpider import *
from DataDryadSpider import *
from multiprocessing import Process

import sys



def harvardWorker(maxDatasets, delay):
    harvardSpiderDelay = 20
    spider = HarvardSpider(harvardSpiderDelay, "output/HarvardData.json")
    spider.crawl(maxDatasets)

def zenodoWorker(maxDatasets, delay):
    spider = ZenodoSpider(delay, "output/ZenodoData.json")
    spider.crawl(maxDatasets)

def dryadWorker(maxDatasets, delay):
    spider = DataDryadSpider(delay, "output/DryadData.json")
    spider.crawl(maxDatasets)

def figShareWorker(maxDatasets, delay):
    spider = FigShareSpider(delay, "output/FigShareData.json")
    spider.crawl(maxDatasets)

# def omicsdiWorker():
#     spider = OmicsdiSpider(delay, "output/OmicsdiData.json")
#     spider.crawl(maxDatasets)

def main():

    if len(sys.argv) != 3:
        print("Usage: python3 main.py <MaxDatasets> <CrawlerDelay>")
        exit()

    maxDatasets = int(sys.argv[1])
    delay = int(sys.argv[2])

    #harvardProcess = Process(target=harvardWorker)
    zenodoProcess = Process(target=zenodoWorker(maxDatasets, delay))
    dryadProcess = Process(target=dryadWorker(maxDatasets, delay))
    figShareProcess = Process(target=figShareWorker(maxDatasets, delay))
    #omicsdiProcess = Process(target=omicsdiWorker)

    #harvardProcess.start()
    zenodoProcess.start()
    dryadProcess.start()
    figShareProcess.start()
    #omicsdiProcess.start()

    #harvardProcess.join()
    zenodoProcess.join()
    dryadProcess.join()
    figShareProcess.join()
    #omicsdiProcess.join()

if __name__ == '__main__':
    main()