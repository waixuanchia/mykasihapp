import requests
from bs4 import BeautifulSoup
from servicesScraper.serviceScraper import JKMScraper

JKM_NEGERI_URL = 'https://www.jkm.gov.my/jkm/index.php?r=portal/locations&map_type=05&id=VDV6WnF6OVBRbWNNOGJYY1Rnd0pvdz09'
JKM_DAERAH_URL = 'https://www.jkm.gov.my/jkm/index.php?r=portal/locations&map_type=06&id=ZnAyVEdsbHNoSmw4VHVkQ2UzdDlqQT09'

class JKMCrawler:

    def __init__(self,url):
        self.pages = []
        self.soup = None
        self.url = url
    
    def get_pages(self,is_headquater=None):
        page = requests.get(self.url)
        
        if not is_headquater:
            self.soup = BeautifulSoup(page.text,'html.parser')

            html = self.soup.select('div.dataTables_paginate .page')
            self.pages = list(map(lambda link: self.sub_pages(link.findChild('a').attrs['href']),html))
        else:
            self.pages = [page.text]

        return self.get_information()

    def get_information(self):
        jkm_details = [JKMScraper(page).get_services_information() for page in self.pages]
        flatten_jkm = [jkm for jkm_sub_page in jkm_details for jkm in jkm_sub_page]
        return flatten_jkm

            
    def sub_pages(self,link):
        page = requests.get(f'https://www.jkm.gov.my{link}')
        return page.text
        


        

crawler_n = JKMCrawler(JKM_NEGERI_URL).get_pages()
crawler_d = JKMCrawler(JKM_DAERAH_URL).get_pages()
#crawler_h = JKMCrawler()
print(crawler_n)

