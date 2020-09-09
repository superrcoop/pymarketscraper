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
    executable_path=CHROMEDRIVER_PATH, chrome_options=options)


def getInfo():
    """""
    This function collects data from ja-mis and return market prices
    """""

    # marketData=[]
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    marketInfo = soup.find(id="ctl00_ContentPlaceHolder1_weekending")
    return 'Pymarketscraper - JAMIS Current Prices at Local Prices Points for Week Ending '+marketInfo.prettify()
