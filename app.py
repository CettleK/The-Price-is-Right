import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome()


#Store links
target_link = "https://www.target.com/s?searchTerm=playstation+5+console&category=0%7CAll%7Cmatchallpartial%7Call+categories&tref=typeahead%7Cterm%7C0%7Cplaystation+5+console%7Cplaystation+5+console%7C%7C%7Cservice%7C%7C%7C%7C%7Ccontext%7Ecategory_v3&searchTermRaw=playstation+5+"
bestbuy_link = "https://www.bestbuy.com/site/searchpage.jsp?st=playstation+5+console&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
newegg_link = "https://www.newegg.com/p/pl?d=playstation+5+console"


#Seperate defs for each url in the case of one failing

def newegg(driver):
    #Open the browser and navigate to a search engine
    driver.get(newegg_link)
    #Find the relevant listings
    products = driver.find_elements(by = 'XPATH', value = )
    #Prevents browser from closing immediately after opening 
    time.sleep(5)

def bestbuy(driver):
    #Open the browser and navigate to a search engine
    driver.get(bestbuy_link)
    #Prevents browser from closing immediately after opening 
    time.sleep(5)

def target(driver):
    #Open the browser and navigate to a search engine
    driver.get(target_link)
    #Prevents browser from closing immediately after opening 
    time.sleep(5)

newegg(driver)
# bestbuy(driver)
# target(driver)

driver.quit()

