from data_framer import *


url_book_list = 'https://www.goodreads.com/list/show/348.Thrillers'
how_many = 500 

file_name = dataframer(url_book_list,how_many)
print('\n')
print('####'*12)
print('all data saved as {}.csv'.format(file_name))
print('####'*12)
