from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd
url = 'https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=EMATB9EJGQV8WR3ER2BX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1'
import matplotlib.pyplot as plt

def web_scraper(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    
    items = soup.find_all('div',class_='lister-item-content')
    f_names = []
    release = []
    ratings = []
    descriptions = []
    durations = []
    directors = []
    actors = []
    
    for item in items:
        header = item.find('h3')
        try:
            film_name = header.find('a').text
            f_names.append(film_name)
        except:
            pass
        
        try:
            release_date= header.find_all('span')[1].text.replace('(','').replace(')','')
            try:
                release_date = int(release_date)
            except:
                pass
            release.append(release_date)
        except:
            pass

        try:
            rating = float(item.find('div',class_='ratings-bar').find('div').find('strong').text)
            ratings.append(rating)
        except:
            pass
        
        
        info = item.find_all('p')
        try:
            duration = info[0].find('span',class_='runtime').text.split()[0]
            durations.append(int(duration))
        except:
            pass
        
        try:
            dscrpt = info[1].text.replace("\n","")
            descriptions.append(dscrpt)
        except:
            pass
        
        
        makers = info[2].find_all('a')
        try:
            director = makers[0].text             
            directors.append(director)
        except:
            pass
            
        try:
            film_actors = []
            for actor in makers[1:]:
                film_actors.append(actor.text)
            actors.append(film_actors)
        except:
            pass
    release[-1]=2013
    web_data = {
        'film names': f_names,
        'ratings': ratings,
        'release dates': release,
        'descriptions': descriptions,
        'durations':durations,
        'directors':directors,
        'actors':actors
    }

    df = pd.DataFrame(web_data)
    return df
    
    

def normalizer_and_mean(df):
    df['rating normalized'] = (df['ratings']-df['ratings'].min())/ (df['ratings'].max() - df['ratings'].min())
    df['duration normalized'] = (df['durations'] - df['durations'].min()) / (df['durations'].max()- df['durations'].min())
    df['rating mean'] = (df['ratings']-df['ratings'].mean())/(df['ratings'].max()-df['ratings'].min())
    return df
    
def plotter(df):
    fig,ax = plt.subplots(figsize=(10,8))
    ax.scatter(df['release dates'],df['ratings'])
    ax.set_title('ratings of films (by year)')
    ax.set_xlabel('years')
    ax.set_ylabel('ratings')
    

def director_films_plotter(df):
    df['film_count'] =1
    df=df[['directors','film_count']].groupby(['directors']).sum()
    fig,ax = plt.subplots()
    ax.scatter(df.index,df['film_count'])
    ax.set_title('number of top100 films of directors')
    ax.set_xlabel('film number')
    ax.set_ylabel('director')
    plt.tight_layout()
    
df = web_scraper(url)

print(normalizer_and_mean(df))
plotter(df)
director_films_plotter(df)
