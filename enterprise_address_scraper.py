from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import logging
from enterprise_name_fix import fix_name
import urllib


class data_mine:

    def __init__(self, web_page):
        # Webpage html, that is going to be data mined.
        self.web_page = web_page

    def mine(self):
        names = fix_name
        # Creates file, to store all the scraped data
        filename = 'enterprise.csv'
        # utf-16 for lithuanian, but using it messes up column separation in CSV
        # utf-8 for ENG
        f = open(filename, "w", encoding="utf-16")
        titles = 'Name,Address\n'  # CSV file column names.
        f.write(titles)
        for index, name in enumerate(names):
            try:
                addresses = {}
                url = "%s"%(self.web_page) + "%s" %(urllib.request.quote(name))
                uClient = uReq(url)
                main_page_html = uClient
                page_soup = soup(main_page_html, 'html.parser')
                # Grabs all the data that certain container has.
                spans = page_soup.findAll("span", {"itemprop": "streetAddress"})
                if spans != []:
                    adresas = spans[0].text
                    addresses[name] = adresas
                else:
                    addresses[name] = 'No info'
                # Write all data  to csv
                f.write('%s,%s\n'
                        % (name,addresses[name],)
                        )
                print(index, 'Succesfully written to csv')
            except Exception as e:
                logging.error("Exception occurred", exc_info=True)
        f.close()

test_1 = data_mine("https://www.1551.lt/paieska/?keyword=")
test_1.mine()



