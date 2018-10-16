import os
import _pickle as pickle
import requests
import extruct
import time
import pprint
from bs4 import BeautifulSoup
from w3lib.html import get_base_url

pp = pprint.PrettyPrinter(indent=2)

class Spider:
    def __init__(self, baseUrl, delay):
        self.baseURL = baseUrl
        self.delay = delay

    def extract_metadata(self, url):
        r = requests.get(url)
        base_url = get_base_url(r.text, r.url)
        data = extruct.extract(r.text.encode('utf8'), base_url=base_url)
        return(data)

    def crawl(self, max_pages):
        page = 0
        url = self.baseURL
        while page < max_pages:
            page += 1
            src = requests.get(url)
            soup = BeautifulSoup(src.text)
            table = soup.find("table", id="resultsTable")
            divs = table.find_all("div", class_="card-title-icon-block")

            # following URL in each row of the table
            for div in divs:
                link = div.find("a")
                nextURL ="https://dataverse.harvard.edu" + link.get('href')
                print( "The URL is :" + nextURL)
                data = self.extract_metadata(nextURL)
                pp.pprint(data)
                time.sleep(30)
    

if __name__ == '__main__':
    baseURL = "https://dataverse.harvard.edu/dataverse/harvard;jsessionid=ea1e4b6aaa41c3d820a98ccecbe0?q=&fq0=metadataSource%3A%22Harvard+Dataverse%22&types=dataverses%3Adatasets&sort=dateSort&order=desc"
    spider = Spider(baseURL, 20)
    spider.crawl(1)





    


