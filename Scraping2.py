from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.chrome.service import Service
import time
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
sphone_table = pd.DataFrame(columns=['Name', 'Price', 'Rating', 'Feedback'])
URL = "https://www.technodom.kz/search?r46_input_query=Samsung&r46_search_query=samsung&recommended_by=instant_search&recommended_code=samsung&page=1&rees46_search_filters=%7B%7D&rees46_search_categories=smartfony"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
ginfo = soup.findAll(class_="ProductCardV_card__pIoz2 ProductItem_product__HR8Z9")
for info in ginfo:
    name = info.find('p', attrs={'class', 'Typography ProductCardV_title__rFAYr ProductCardV_loading__TkTOe Typography__M'}).text
    price = info.find('p', attrs={'class', 'Typography ProductCardPrices_price__5dlTx Typography__Subtitle'}).text.replace(u'\xa0', '')
    try:
        rating = info.find('p', attrs={'class', 'Typography RatingAndReviewsCount_rating__xG62B Typography__M Typography__M_Bold'}).text
    except:
        rating = np.nan
    try:
        feedback = info.find('p', attrs={'class', 'Typography RatingAndReviewsCount_review__EiJSu Typography__M'}).text
    except:
        feedback = '-'
    data = [name, price, rating, feedback]
    sphone_table.loc[len(sphone_table)] = data
sphone_table.to_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Table2.csv')