from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd


url = 'https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

item= soup.find('div',class_='DailyForecast--DisclosureList--msYIJ')
boxes = item.find_all('div',class_='DaypartDetails--Content--hJ52O DaypartDetails--contentGrid--1SWty')
high_temps = []
low_temps = []
descrpts = []
w_days = []
def converter(f):
        temp_int = int(f.split('°')[0])
        cel = round(5*(temp_int-32)/9)
        return cel

for box in boxes[1:]:#as first box, consists of only night, we ll skip it
    day_item = box.find_all('div')[0].find('h3').text.split(" ")[0]
    w_days.append(day_item)
    temp_high = converter(box.find_all('div',)[0].find('div').find('div').get_text())
    high_temps.append(temp_high)
    #print(temp_high)
    temp_low = converter(box.find_all('div',class_='DailyContent--DailyContent--KcPxD')[1].find('div').find('div').text)
    low_temps.append(temp_low)
    descrpt = box.find_all('div')[0].find('p').text
    descrpts.append(descrpt)
    

data = {
    'days': w_days,
    "high": high_temps,
    "low": low_temps,
    "description":descrpts
}

dti = pd.date_range("2021-09-29",periods=len(data['days']),freq='B')
    
df = pd.DataFrame(data,index=dti)
    
print(df)
    
