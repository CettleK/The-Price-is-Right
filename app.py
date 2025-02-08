import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome()


target_link = "https://www.target.com/s?searchTerm=playstation+5+console"
bestbuy_link = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&st=playstation+5+console"
newegg_link = "https://www.newegg.com/p/pl?d=playstation+5+console"

# product = input("What are you searching for?")
# productplus = product.replace(" ", "+")

#Store links
#newegg_link = "https://www.newegg.com/p/pl?d=" + productplus
#bestbuy_link = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&st=" + productplus
#target_link = "https://www.target.com/s?searchTerm=" + productplus

#Seperate defs for each url in the case of one failing

def newegg(driver):
    #Open the browser and navigate to a search engine
    driver.get(newegg_link)

    #Find product listings
    # item_cell = '//div[contains(@class, "item-cell")]'
    #Collect title and price (.// is for finding an element within item_cell)
    # item_name = './/a[contains(@class, "item-title")]'
    # item_price = './/li[contains(@class, "price-current")]'

    #Find the relevant listings
    products = driver.find_elements(By.XPATH, value = '//div[contains(@class, "item-cell")]')
    
    ne_item = []
    ne_price = []

    for x in products:
        # print(x.find_element(By.XPATH, value = './/a[contains(@class, "item-title")]').text)
        ne_item.append(x.find_element(By.XPATH, value = './/a[contains(@class, "item-title")]').text)
        # print(x.find_element(By.XPATH, value = './/li[contains(@class, "price-current")]').text)
        ne_price.append(x.find_element(By.XPATH, value = './/li[contains(@class, "price-current")]').text)
    
    #Remove dollar signs from price 
    #fixed_ne_price = sorted(ne_price, key=lambda price: float(price.replace("$", "")))
    #Sort starting from cheapest
    #merge_ne_item = sorted(zip(ne_price, ne_item), key=lambda pair: pair[0])

    #print(ne_price)

    #Combines and removes dollar signs to sort values
    merge_ne_item = sorted(zip(ne_price, ne_item), key=lambda pair: float(pair[0].replace("$", "").replace(" ", "")))
    ne_price, ne_item = zip(*merge_ne_item)

    for i in range(len(ne_item)):
        print(ne_item[i], ne_price[i])

    #Prevents browser from closing immediately after opening 
    time.sleep(5)

def bestbuy(driver):
    #Open the browser and navigate to a search engine
    driver.get(bestbuy_link)

    #Find product listings
    # item_cell = '//div[contains(@class, "item-cell")]'
    #Collect title and price (.// is for finding an element within item_cell)
    # item_name = './/a[contains(@class, "item-title")]'
    # item_price = './/li[contains(@class, "price-current")]'

    #Find the relevant listings
    products = driver.find_elements(By.XPATH, value = '//li[contains(@class, "sku-item")]')
    
    bb_item = []
    bb_price = []

    for x in products:
        #print(x.find_element(By.XPATH, value = './/h4[contains(@class, "sku-title")]').text)
        bb_item.append(x.find_element(By.XPATH, value = './/h4[contains(@class, "sku-title")]').text)
        
        price = x.find_element(By.XPATH, value = './/div[contains(@class, "priceView-hero-price priceView-customer-price")]')
        
        #print(price.find_element(By.XPATH, value = './/span[@aria-hidden="true"]').text)
        bb_price.append(price.find_element(By.XPATH, value = './/span[@aria-hidden="true"]').text)
    
    #Remove dollar signs from price 
    #fixed_ne_price = sorted(ne_price, key=lambda price: float(price.replace("$", "")))
    #Sort starting from cheapest
    #merge_ne_item = sorted(zip(ne_price, ne_item), key=lambda pair: pair[0])

    #Combines and removes dollar signs to sort values
    merge_bb_item = sorted(zip(bb_price, bb_item), key=lambda pair: float(pair[0].replace("$", "").replace(" ", "")))
    bb_price, bb_item = zip(*merge_bb_item)

    for i in range(len(bb_item)):
        print(bb_item[i], bb_price[i])


    #Prevents browser from closing immediately after opening 
    time.sleep(5)

def target(driver):
    #Open the browser and navigate to a search engine
    driver.get(target_link)

     #Find the relevant listings
    products = driver.find_elements(By.XPATH, value = '//div[contains(@class, "styles_ndsCol")]')
    
    t_item = []
    t_price = []

    for x in products:
        print(x.find_element(By.XPATH, value = '//div[contains(@class, "styles_ndsTruncate__GRSDE")]').text)
        t_item.append(x.find_element(By.XPATH, value = './/div[contains(@class, "styles_ndsTruncate__GRSDE")]').text)
        #print(x.find_element(By.XPATH, value = './/span[contains(@class, "sc-f9ebbc4c-3 duMaUK h-text-bold h-text-lg h-margin-r-tiny h-text-nowrap")]').text)
        #t_price.append(x.find_element(By.XPATH, value = './/span[contains(@class, "sc-f9ebbc4c-3 duMaUK h-text-bold h-text-lg h-margin-r-tiny h-text-nowrap")]').text)
    
    #Combines and removes dollar signs to sort values
    # merge_t_item = sorted(zip(t_price, t_item), key=lambda pair: float(pair[0].replace("$", "").replace(" ", "")))
    # t_price, t_item = zip(*merge_t_item)

    # for i in range(len(t_item)):
    #     print(t_item[i], t_price[i])

    #Prevents browser from closing immediately after opening 
    time.sleep(5)

# newegg(driver)
# bestbuy(driver)
target(driver)

driver.quit()
