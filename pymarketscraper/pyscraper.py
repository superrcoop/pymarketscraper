from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
# marketData=[]
driver.get("http://www.ja-mis.com/Companionsite/home.aspx")
content = driver.page_source
soup = BeautifulSoup(content)
marketData = soup.find(id="hor-minimalist-b")
print(marketData.prettify())
