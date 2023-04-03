import re
from bs4 import BeautifulSoup

class InfoMinistries:

    def __init__(self,jkm_details,jkm_obj):
        self.jkm_details = jkm_details
        self.jkm_obj = jkm_obj
        

    def get_lat_long(self):
        return self.jkm_obj.select_one('div div:last-child a').attrs['href']
    
    def get_details(self):

        [office,address,tels,faks,emel,*_] = filter(lambda str: re.search('\w',str),re.split('\n+',self.jkm_details))
        
        return {
            'office':office,
            'address':address,
            'tels':re.sub(' *Tels? *:','',tels),
            'faks':re.sub(' *Faks? *:','',faks),
            'emel':re.sub(' *Emels? *:','',emel),
            'lat':re.split('\,',re.sub('http://maps\.google\.com/\?q\=','',self.get_lat_long()))[0],
            'long':re.split('\,',re.sub('http://maps\.google\.com/\?q\=','',self.get_lat_long()))[1]

        }


class JKMScraper:

    def __init__(self,page):
        self.page = page
        self.soup = None

    def get_services_information(self):
        self.soup = BeautifulSoup(self.page,'html.parser')

        jkm_informations = self.soup.select('.portal-map td')
        jkm_informations_str = list(map(lambda td: td.text,jkm_informations))
        
        
        jkm_details = [InfoMinistries(jkm,jkm_informations[index]).get_details() for index, jkm in enumerate(jkm_informations_str)]
        return jkm_details



        
        