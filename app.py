import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome()


# Open the browser and navigate to a search engine
driver.get("https://www.amazon.com/")

#Prevents browser from closing immediately after opening 
time.sleep(5)

driver.quit()

