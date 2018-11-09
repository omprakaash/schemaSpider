from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *
from ZenodoSpider import *
from DataDryadSpider import *

from multiprocessing import Process

delay = 15
maxDatasets = 20

def harvardWorker():
    harvardSpiderDelay = 20
    spider = HarvardSpider(harvardSpiderDelay, "HarvardData.json")
    spider.crawl(maxDatasets)

def zenodoWorker():
    spider = ZenodoSpider(delay, "ZenodoData.json")
    spider.crawl(maxDatasets)

def dryadWorker():
    spider = DataDryadSpider(delay, "DryadData.json")
    spider.crawl(maxDatasets)

def figShareWorker():
    spider = FigShareSpider(delay, "FigShareData.json")
    spider.crawl(maxDatasets)

def omicsdiWorker():
    spider = OmicsdiSpider(delay, "OmicsdiData.json")
    spider.crawl(maxDatasets)

def main():
    harvardProcess = Process(target=harvardWorker)
    zenodoProcess = Process(target=zenodoWorker)
    dryadProcess = Process(target=dryadWorker)
    FigShareProcess = Process(target=figShareWorker)
    omicsdiProcess = Process(target=omicsdiWorker)

    harvardProcess.start()
    zenodoProcess.start()
    dryadProcess.start()
    figShareProcess.start()
    omicsdiProcess.start()

    harvardProcess.join()
    zenodoProcess.join()
    dryadProcess.join()
    figShareProcess.join()
    omicsdiProcess.join()

if __name__ == '__main__':
    main()