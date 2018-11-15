from HarvardSpider import *
from FigShareSpider import *
from OmicsdiSpider import *
from ZenodoSpider import *
from DataDryadSpider import *

from multiprocessing import Process

delay = 15
maxDatasets = 35

def harvardWorker():
    harvardSpiderDelay = 20
    spider = HarvardSpider(harvardSpiderDelay, "out/HarvardData.json")
    spider.crawl(maxDatasets)

def zenodoWorker():
    spider = ZenodoSpider(delay, "out/ZenodoData.json")
    spider.crawl(maxDatasets)

def dryadWorker():
    spider = DataDryadSpider(delay, "out/DryadData.json")
    spider.crawl(maxDatasets)

def figShareWorker():
    spider = FigShareSpider(delay, "out/FigShareData.json")
    spider.crawl(maxDatasets)

# def omicsdiWorker():
#     spider = OmicsdiSpider(delay, "OmicsdiData.json")
#     spider.crawl(maxDatasets)

def main():
    harvardProcess = Process(target=harvardWorker)
    # zenodoProcess = Process(target=zenodoWorker)
    # dryadProcess = Process(target=dryadWorker)
    # figShareProcess = Process(target=figShareWorker)
    #omicsdiProcess = Process(target=omicsdiWorker)

    harvardProcess.start()
    # zenodoProcess.start()
    # dryadProcess.start()
    # figShareProcess.start()
    #omicsdiProcess.start()

    harvardProcess.join()
    # zenodoProcess.join()
    # dryadProcess.join()
    # figShareProcess.join()
    #omicsdiProcess.join()

if __name__ == '__main__':
    main()