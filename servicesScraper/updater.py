from ministries.models import Ministries,Regions
from servicesScraper.servicesCrawler import crawler_n,crawler_d

def updater():
    headquaters = Regions.objects.create(types='Headquaters')
    state = Regions.objects.create(types='state')
    district = Regions.objects.create(types='district')

    headquaters.save()
    state.save()
    district.save()

    loop_(crawler_n,state)
    loop_(crawler_d,district)
        

def loop_(ministries,type):
    for ministry in ministries:
        ministry_ob = create_ministry(ministry,type)
        ministry_ob.save()
        


def create_ministry(ministry,type):
    ministry = Ministries.objects.create(office=ministry['office'],address=ministry['address'],tels=ministry['tels'],faks=ministry['faks'],emel=ministry['emel'],latitude=ministry['lat'],longitude=ministry['long'])
    ministry.region = type
    
    return ministry
