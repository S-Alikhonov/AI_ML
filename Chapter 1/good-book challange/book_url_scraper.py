from selenium import webdriver
from time import sleep
def link_scraper(main_url,how_many):
    driver = webdriver.Chrome()

    """

    this function takes url (string) and final_page(integer)
    srapes individual book url, targeting the href attribute of the book.
    returns the resulst, as a list of urls, scraped till the page user input as an argument
    
    """
    if ( how_many == 0 ) or ( type(how_many) !=int ):
        return None
    elif how_many%100 >0:
        pages = how_many//100 + 1
    elif how_many//100 and how_many !=0:
        pages = how_many // 100
    print('****'*12)
    print('scraping individual links has been started.')
    print('****'*12)
    print('\n')

    urls = [[],[],[]]
    for i in range(pages):
        url = main_url+"page={}".format(i+1)
        driver.get(url)
        if i==0:
            cat_name = driver.find_element_by_xpath('//h1[@class="gr-h1 gr-h1--serif"]').text
            urls[2].append(cat_name)
            print('category:{}'.format(cat_name))
            print('----'*12)
            max_page = driver.find_element_by_xpath('//div[@class="pagination"]').find_elements_by_tag_name('a')[-2].text
            print('There are more than {} books in this list'.format((int(max_page)-1)*100))
        if pages>int(max_page):
            print('\n')
            print('as you can see, there are less than {} books'.format(how_many))
            print('####'*12)
            return None
        
        book_table = driver.find_element_by_xpath('//table[@class="tableList js-dataTooltip"]')#targets the box that contains the list of books
        books = book_table.find_elements_by_tag_name('tr')#targets each and every book
        for book in books:
            info_box = book.find_elements_by_tag_name('td')
            info = info_box[2]#targets the box containing info about the book
            pctr = info_box[1].find_elements_by_tag_name('div')[1].find_element_by_tag_name('a').find_element_by_tag_name('img')
            b_title = info.find_element_by_class_name('bookTitle')#targets title of the book, and extracts href as url from it
            
            urls[0].append(b_title.get_attribute('href'))
            urls[1].append(pctr.get_attribute('src'))
        sleep(1)
    print('\n')
    print('*'*50)
    print('indvidual urls of {} books have scraped seccessfully!'.format(how_many))
    print('*'*50)
    driver.quit()
    return urls



