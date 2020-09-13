from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.common.by import By

chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('headless')
chrome_options.binary_location = chrome_bin
driver = webdriver.Chrome()
# driver = webdriver.Chrome(
#   executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


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
    json_array = get_fruits_prices() + get_crops_prices() + get_herbs_prices() + \
        get_legumes_prices() + get_veg_prices()
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
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '', 'Category': 'Fruits',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    return json_array


def get_herbs_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    element = driver.find_element_by_id(
        'ctl00_ContentPlaceHolder1_ddl_CategoryName')
    select = Select(element)
    select.select_by_index(1)
    WebDriverWait(driver, 10).until(EC.staleness_of(element))
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '', 'Category': 'Herbs & Spices',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    return json_array


def get_legumes_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    element = driver.find_element_by_id(
        'ctl00_ContentPlaceHolder1_ddl_CategoryName')
    select = Select(element)
    select.select_by_index(2)
    WebDriverWait(driver, 10).until(EC.staleness_of(element))
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '', 'Category': 'Legumes',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    return json_array


def get_crops_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    element = driver.find_element_by_id(
        'ctl00_ContentPlaceHolder1_ddl_CategoryName')
    select = Select(element)
    select.select_by_index(3)
    WebDriverWait(driver, 10).until(EC.staleness_of(element))
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '', 'Category': 'Root Crops',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    return json_array


def get_veg_prices():
    """""
    This function collects data from ja-mis and return market prices
    """""
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    element = driver.find_element_by_id(
        'ctl00_ContentPlaceHolder1_ddl_CategoryName')
    select = Select(element)
    select.select_by_index(4)
    WebDriverWait(driver, 10).until(EC.staleness_of(element))
    content = driver.page_source
    marketInfo = BeautifulSoup(content, features="html.parser")
    json_array = []

    for row in marketInfo.find(id="hor-minimalist-b").tbody.find_all('tr'):
        json_data = {'Item': '', 'Type': '', 'FarmGate': '', 'Category': 'Vegetables',
                     'Municipal': '', 'Wholesale': '', 'Retail': ''}
        if row.get_text():
            for idx, td in enumerate(row.find_all('td')):
                json_data[list(json_data)[idx]] = td.get_text()
            json_array.append(json_data)
    return json_array
