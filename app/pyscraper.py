from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
chrome_options.binary_location = chrome_bin
#driver = webdriver.Chrome()
driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


def getInfo():
    """""
    This function collects data from ja-mis and return market report ending date
    """""

    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    marketInfo = soup.find(id="ctl00_ContentPlaceHolder1_weekending")
    return 'Pymarketscraper - JAMIS Current Prices at Local Prices Points for Week Ending '+marketInfo.prettify()


def get_all_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""

    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    marketInfoDate = marketInfo.find(id="ctl00_ContentPlaceHolder1_weekending")
    json_array = []
    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    if not json_array:
        json_obj = {'status': '404', 'message': 'not found',
                    'request': 'GET /api/v1/marketInfo/prices', 'data': []}
    else:
        json_obj = {'status': '200', 'message': 'success', 'date': marketInfoDate.get_text(),
                    'request': 'GET /api/v1/marketInfo/prices', 'data': json_array}
    # print(json_array)
    return json_obj


def get_fruits_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    marketInfoDate = marketInfo.find(id="ctl00_ContentPlaceHolder1_weekending")
    categorySelect = marketInfo.find(
        id="ctl00_ContentPlaceHolder1_ddl_CategoryName")
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    if not json_array:
        json_obj = {'status': '404', 'message': 'not found',
                    'request': 'GET /api/v1/marketInfo/prices', 'data': []}
    else:
        json_obj = {'status': '200', 'message': 'success', 'date': marketInfoDate.get_text(),
                    'request': 'GET /api/v1/marketInfo/prices', 'data': json_array}
    # print(json_array)
    return json_obj
