from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def getInfo():
    """""
    This function collects data from ja-mis and return market prices
    """""
    options = webdriver.ChromeOptions()

    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    # IWebDriver driver = new ChromeDriver(options)
    # marketData=[]
    driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    marketData = soup.find(id="hor-minimalist-b")
    return marketData.prettify()
