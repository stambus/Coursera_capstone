from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import time

class data_mine:

    def __init__(self, web_page):
        # Webpage html, that is going to be data mined.
        self.web_page = web_page

    def mine(self):
        # That's the number of pages we are gonna scrape thru. Need to find better way.
        page_num = 128
        # Looped
        items_looped = []
        # Creates file, to store all the scraped data
        filename = 'flats.csv'
        # utf-16 for lithuanian, but using it messes up column separation in CSV
        # utf-8 for ENG
        f = open(filename, "w", encoding="utf-8")
        headers = 'Adresas , Rajonas, Kambarių sk, Plotas, Kaina, Šildymas, Pastato tipas, Metai\n'  # CSV file column names.
        f.write(headers)
        for i in range(page_num):
            # Gonna calculate how much time, is it gonna take to loop thru 1 page
            start_time = time()
            # Main pages URL
            main_url = "%s/%s" %(self.web_page, i)
            uClient = uReq(main_url)
            main_page_html = uClient

            # Parses all of the data that particular html has
            page_soup = soup(main_page_html, 'html.parser')

            # Grabs all the data that certain container has.
            containers = page_soup.findAll("tr", {"class": "list-row"})

            # Loops thru pages designated container and gets required data.
            for container in containers:
                try:
                    flat_href = container.a['href']
                    flat_title = container.a.img['alt']
                    new_lookup_url = 'https://www.aruodas.lt/{0}'.format(flat_href)
                    new_lookup_page_html = uReq(new_lookup_url)
                    # Parses all of the data that particular new look html has
                    new_lookup_page_soup = soup(new_lookup_page_html, 'html.parser')
                    # Parses flat's price from html.
                    flat_price = new_lookup_page_soup.findAll('span', {'class': "price-eur"})[0].text.replace(" ", "")
                    flat_price = float(flat_price[:-1])
                    # Flats adress and neighbourhood
                    flat_adress = flat_title.split(",")[1]
                    flat_neighbourhood = flat_title.split(",")[0]
                    # Empty lists, needed to create flat's detail dictionary.
                    dt_tag_list = []
                    dd_tag_list = []
                    # Looping thru container that has all of the detail names.
                    # These are gonna be key's inside our details dictionary.
                    for dt_tag in new_lookup_page_soup.findAll('dt'):
                        flat_details_raw_text_dt = dt_tag.text.replace(' ', "").replace('\n', "").replace(':',
                                                                                                          "").replace(
                            '.',
                            "")
                        dt_tag_list.append(flat_details_raw_text_dt)
                    # Looping thru container that has all of the detail values.
                    # These are gonna be values inside our details dictionary.
                    for dd_tag in new_lookup_page_soup.findAll('dd'):
                        flat_details_raw_text_dd = dd_tag.text.replace(' ', "").replace('\n', "").replace(',', '.')
                        dd_tag_list.append(flat_details_raw_text_dd)
                    # Zips generated new lists of detail names and values to dictionary.
                    flat_details_dict = dict(zip(dt_tag_list, dd_tag_list))
                    # Writing to CSV file
                    f.write(
                        flat_adress + "," +
                        flat_neighbourhood + "," +
                        flat_details_dict['Kambariųsk'] + "," +
                        flat_details_dict['Plotas'][:-2] + "," +
                        str(flat_price) + "," +
                        flat_details_dict['Šildymas'] + "," +
                        flat_details_dict['Pastatotipas'] + "," +
                        flat_details_dict['Metai'] + "," +
                        "\n")

                    # Time it takes to loop
                    end_time = time()
                    total_time = end_time - start_time
                    # Items alredy looped
                    items_looped.append("Succes")
                    print('%s advertisment succesfully written to CSV' % len(items_looped))
                except:
                    print('Error occurred, skiping to other advertisment')
            print("It took %s seconds to loop %s page" % (total_time, i))
        f.close()


test_1 = data_mine("https://www.aruodas.lt/butai/vilniuje/puslapis/")
test_1.mine()

