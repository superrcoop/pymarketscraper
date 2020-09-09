from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os


def getInfo():
    """""
    This function collects data from ja-mis and return market prices
    """""

    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('headless')
    chrome_options.binary_location = chrome_bin
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    # marketData=[]
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    marketData = soup.find(id="hor-minimalist-b")
    return marketData.prettify()
