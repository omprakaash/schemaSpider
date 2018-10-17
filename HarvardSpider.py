from Spider import *

class HarvardSpider(Spider):
    def __init__(self, baseURL, delay):
        super().__init__(baseURL, delay)

    def crawl(self, maxPages):
        
        curPage = 1
     
        while curPage <= maxPages:
            
            url = self.baseURL + str(curPage)

            src = requests.get(url)
            soup = BeautifulSoup(src.text)
            table = soup.find("table", id="resultsTable")
            divs = table.find_all("div", class_="card-title-icon-block")

            # following URL in each row of the table
            for div in divs:
                link = div.find("a")
                nextURL ="https://dataverse.harvard.edu" + link.get('href')
                print( "The URL is :" + nextURL)
                data = super().extract_metadata(nextURL)
                pp.pprint(data)
                time.sleep(self.delay)
            
            curPage += 1
    