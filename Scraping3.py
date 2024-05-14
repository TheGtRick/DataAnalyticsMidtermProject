from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
table = pd.DataFrame(columns=['Date', 'Price', 'Open', 'High', 'Low', 'Vol', 'Change'])
URL = "https://www.investing.com/equities/xiaomi-historical-data"
driver.get(URL)
driver.find_element(By.XPATH, "//*[@id='__next']/header/div[1]/section/div[3]/ul/li[1]/button").click()
driver.find_element(By.XPATH, "//*[@class='bp3-portal']/div/div[2]/div/form/button[3]").click()
driver.find_element(By.XPATH, "//*[@class='bp3-portal']/div/div[2]/div/form/div[3]/input").send_keys("220107020@stu.sdu.edu.kz")
driver.find_element(By.XPATH, "//*[@class='bp3-portal']/div/div[2]/div/form/div[5]/input").send_keys("RZ12345")
driver.find_element(By.XPATH, "//*[@class='bp3-portal']/div/div[2]/div/form/button").click()
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]").click()
except:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]").click()
try:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div/div[2]").click()
except:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]").click()
try:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div").click()
except:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div").click()
try:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/input").__setattr__('value', '2018-01-01')
except:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/input").__setattr__('value', '2018-01-01')
try:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]").click()
except:
    driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]").click()
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
data = soup.find_all("tr", class_="h-[41px] hover:bg-[#F5F5F5] relative after:absolute after:bottom-0 after:bg-[#ECEDEF] after:h-px after:left-0 after:right-0 historical-data-v2_price__atUfP")
for info in data:
    date = info.select_one("td:nth-of-type(1)").text
    price = float(info.select_one("td:nth-of-type(2)").text) * 0.12
    open = float(info.select_one("td:nth-of-type(3)").text) * 0.12
    high = float(info.select_one("td:nth-of-type(4)").text) * 0.12
    low = float(info.select_one("td:nth-of-type(5)").text) * 0.12
    vol = info.select_one("td:nth-of-type(6)").text
    change = info.select_one("td:nth-of-type(7)").text
    data = [date, price, open, high, low, vol, change]
    table.loc[len(table)] = data
table.to_csv('C:\\Users\\Rakon\\Desktop\\Midterm Project\\Xiaomi.csv')