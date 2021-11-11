import pandas as pd
from selenium import webdriver
from time import sleep

def scraper(url_path):
    """
    scraper function takes list of urls (strings) as an argument
    targets the title, average rating, number of ratings, number of reviews,
    number of pages, publication year and first publication year, whether book belongs
    to the book series, genres, awards.

    extracts those values, stores into separate lists, then creates the dictionary from them.
    Returns the result as a dictionary.
    """
    column_names = ["titles","author","number_of_reviews","number_of_ratings","average_rating","number_of_pages","published_year",\
        "first_published","series","genres","awards","places","url","cover_url"]
    ress = pd.DataFrame(columns=column_names)
    # titles = []
    # avg_ratings = []
    # authors = []
    # num_ratings = []
    # num_revs = []
    # num_pages = []
    # publ_years = []
    # is_series = []
    # genres = []
    # awards = []
    # places = []
    # pub_years_1 = []
    # book_urls = []
    ################ starting point ############################
    print('\n'*2)
    print('*--*'*12)
    print('Individual book scraping has been started')
    print('*--*'*12)
    driver = webdriver.Chrome()
    counter = 0 # counter used to count number of books scraped
    pl_check = 0
    place = []
    for url in url_path:
        data={}
        counter +=1 # counter increment
        if counter %25==0: #when each 25 pile scraped, it prints and sleeps for 2 secs
            print('{} books have been scraped'.format(counter))
            print('----'*12)
            if counter%100==0:
                sleep(3) #it sleep extra 3 secs, when a 100 books' pile are done
            sleep(2)
        driver.get(url)#loads the each individual page
        try:
            cover= driver.find_element_by_id('coverImage').get_attribute('src')
            data['cover_url']=cover
            box = driver.find_element_by_id('metacol')
            ######## extracting info about title ##############
            title = box.find_element_by_id('bookTitle').text #targets unique item with id 
            data['titles']=title
            ######## extracting info about average rating ##############
            author_box = box.find_element_by_id('bookAuthors') #targets box containing author info
            author = author_box.find_elements_by_tag_name('a')[0].text
            data['author']=author
            ######## extracting info about average rating ##############
            rat_rev_box = box.find_element_by_id('bookMeta') # targets the box containing info about ratings, reviews
            avg_rating = rat_rev_box.find_elements_by_tag_name('span')[6].text#Targets the 7th span as it holds avg_rating info
            data['average_rating']=float(avg_rating)
            ######## extracting info about number of ratings ##############
            num_rating = rat_rev_box.find_elements_by_tag_name('a')[1].text.split()[0].replace(',','')
            data['number_of_ratings']=int(num_rating)
            ######## extracting info about number of reviews ##############
            num_rev = rat_rev_box.find_elements_by_tag_name('a')[2].text.split()[0].replace(',','')
            data['number_of_reviews']=int(num_rev)
            ########## finds element containing pages, pub year
            details = box.find_element_by_id('details') #targets details box containing info about a book
            ######## is it aprt of book series ################
            series = box.find_element_by_id('bookSeries')
            if len(series.text)>0: #checks whether bookSeries text exists or not
                data['series']=True
            else:
                data['series']=False
            ######## extracting info about pages ##############
            page_check = 0
            try:
                #targets item with itemrop = 'numberOfPages'
                pages = details.find_elements_by_tag_name('div')[0].find_element_by_xpath('.//span[@itemprop="numberOfPages"]').text.split()
                for i in pages:
                    if i.isnumeric(): #check if it is numeric
                        data['number_of_pages']=int(i)
                        page_check=1 #make check mask 1
                        break
            except:
                pass
            if not page_check: #if mask never change, the value will be None
                data['number_of_pages']=None
            ####### extracting info about pub year ##############
            year_check = 0
            try:
                years_info = details.find_elements_by_tag_name('div')[1]
                pub_years = years_info.text.split()
                for year in pub_years:
                    if len(year)==4 and year.isnumeric():#if it has length of 4 and integer, it will be a year
                        data['published_year']=int(year)
                        year_check = 1
            except:
                pass
            if not year_check:
                data['published_year']=None
            ####### extracting info about pub year first ##############
            year_check_1 = 0
            try:
                pub_years_first = years_info.find_elements_by_class_name('greyText')[0].text.replace('(','').replace(')','').split()
                for yr in pub_years_first:
                    if len(yr)==4 and yr.isnumeric():
                        data['first_published']=int(yr)
                        year_check_1 = 1
            except:
                pass
            if not year_check_1:
                data['first_published']=None
            ######## extracting info about genre ##############
            genre_check = 0
            try:
                genres_box = driver.find_element_by_xpath('//div[@class="stacked"]').\
                    find_element_by_xpath('.//div[@class="bigBoxContent containerWithHeaderContent"]').\
                    find_elements_by_class_name('elementList')[:3] #targets first 3 genre items
                genre_complete=[]
                
                for genre in genres_box: #extracts text and merges them
                    genre_complete.append(genre.find_elements_by_tag_name('div')[0].text)
                data['genres']=genre_complete
                genre_check=1
                
            except:
                pass
            if not genre_check :
                data['genres']=None
            ######## extracting info about awards ##############
            more_info_button = details.find_element_by_id('bookDataBoxShow')
            try:
                more_info_button.click()
            except:
                pass
            check = 0

            award_places = details.find_elements_by_tag_name('div')[2].find_elements_by_tag_name('div')[0]
            try: #comment out from here else included, if you want aslo click more... button and scrape elements from there
                award_box = award_places.find_elements_by_class_name('clearFloats')
                complete_award = []
                for box in award_box:
                    check = 0
                    try: # targets on item with itemprop = 'awards'
                        award_list = box.find_element_by_xpath('.//div[@itemprop="awards"]').find_elements_by_xpath('.//a[@class="award"]')
                        for l in award_list:
                            complete_award.append(l.text)
                        # for ind_award in award_list:
                        #     complete_award.append(ind_award.text())
                        check = 1
                    except:
                        pass
            except:
                pass
            if not check:
                data['awards']=None
            else:
                data['awards']=complete_award
                check=0

            ### !!! then uncomment code below

            # try:
            #     award_box = award_places.find_elements_by_class_name('clearFloats')
            #     for box in award_box:
            #         check = 0
            #         try:
            #             award = box.find_element_by_xpath('.//div[@itemprop="awards"]')
            #             more_bttn = award.find_elements_by_tag_name('span')[0].find_elements_by_class_name('actionLinkLite')[0]
            #             print('clicked')
            #             more_bttn.click()
            #             check = 1
            #         except:
            #             pass
            # except:
            #     pass
            # if not check:
            #     awards.append(None)
            # else:
            #     awards.append(award.text.replace('...less',''))
            #     check=0
            ####### extracting info about places ##############
            settings = award_places.find_elements_by_class_name('infoBoxRowItem')
            for setting in settings:
                plcs = setting.find_elements_by_tag_name('a')
                for plc in plcs:
                    linking = plc.get_attribute('href')#extracts href attribute
                    if '/places/' in linking: #check if it contains /places/
                        place.append(plc.text)
                        pl_check =1

            if not pl_check:
                data['places']=None
            else:
                data['places']=place
                # place=[]
            pl_check = 0
            data['url']=url
        except:
            pass
        # data = {
        
        # "number_of_reviews":num_revs,
        # "number_of_ratings":num_ratings,
        # "average_rating":avg_ratings,
        # "number_of_pages":num_pages,
        # "published_year":publ_years,
        # "first_published":pub_years_1,
        # "series":is_series,
        # "genres":genres,
        # "awards":awards,
        # "places":places,
        # "url": book_urls
        # }
        print(data)
        ress = ress.append(data,ignore_index=True)
        print(ress)
        
    print('\n'*2)
    print('*--*'*12)
    print('books have been successfully scraped')
    print('*--*'*12)

    return ress
