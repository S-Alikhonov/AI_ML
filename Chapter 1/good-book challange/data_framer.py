import pandas as pd
from book_scraper import *
from book_url_scraper import *

def dataframer(main_url,how_many):

    """
    dataframer function takes starting(int)-starting idex of slicing, 
    ending(int)-ending index of slicing, list of urls (list)
    then calls scraper function, to get the dictionary.
    Then creates dataset from it using pandas DataFrame.
    Stores this dataset as csv file into the hard drive of local machine.
    
    """
    if not link_scraper(main_url,how_many):
        return None
    links,img_links, file_name = link_scraper(main_url,how_many)
    data = scraper(links)
    df = pd.DataFrame(data,dtype=object)
    
    df.to_csv('{}.csv'.format(file_name))

