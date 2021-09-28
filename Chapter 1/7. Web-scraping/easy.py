import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


page = requests.get('https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YVL4FmaA63K')
soup = BeautifulSoup(page.content, 'html.parser')
panel = soup.find_all('div',id='seven-day-forecast-body')[0]

day_lists = panel.find_all('li',class_='forecast-tombstone')[::2]
night_lists = panel.find_all('li',class_='forecast-tombstone')[1::2]

#------------------------
def converter(f):
        temp_int = int(f.split(' ')[1])
        cel = round(5*(temp_int-32)/9)
        return cel

high_temp=[]
low_temp =[]
week_day = []
descriptions = []

for li in day_lists:
    high_temp_f = li.find('p',class_='temp temp-high').get_text()
    high_c = converter(high_temp_f)
    high_temp.append(high_c)

    #above code, tries to get high temp values, using function converts into integer and celcius, returns it
    dow = li.find('p',class_='period-name').get_text()
    week_day.append(dow)

    #code above, implements the scraping the name of the day of week

    dscr = li.find_all('p')[1].find('img')['title'].split(':')[1]
    descriptions.append(dscr)

    """in p tags, there is img tag, in img tag there is useful for
    description. accessing it. then there is extra name of the week days followed by ":"
    so using split and taking second element from it, we basically extracting the useful text for us """

for li in night_lists:
    high_temp_f = li.find('p',class_='temp temp-low').get_text()
    low_c = converter(high_temp_f)
    low_temp.append(low_c)
low_temp.append(None) # as there is no data avaliable for 5th entry
# loop above tries to extract low temp values

#------------------------------------
data = {"week-day": week_day,
        "high": high_temp,
        "low": low_temp,
        "description": descriptions
}

dti = pd.date_range('2021-09-28',periods=5,freq='D')

my_scraps = pd.DataFrame(data, index=dti)
print(my_scraps)

    




 