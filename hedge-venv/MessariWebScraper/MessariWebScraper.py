from genericpath import exists
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import requests


    
def GrabMessariData(website, driver):

    driver.get(website)
    driver.implicitly_wait(5)
    time.sleep(2) #depending on load time we get an incorrect web page title, so we sleep, *we want title because it can tell us which hedgefund we are viewing"
    hedgeName = driver.title
    print("Hedgefund: ",hedgeName)

    WebDriverWait(driver, timeout=10).until(
    ec.visibility_of_element_located((By.XPATH, "//*[@id='root']//*[contains(@class,'infinite-window')]/div/div/div[2]"))
    )

    rawCSS = driver.find_elements(By.XPATH, "//*[@id='root']//*[contains(@class,'infinite-window')]/div/div/div[2]") #get the raw css
    lines = [] #used to filter out CSS text line by line, *contains alot of junk lines*
    coinNames = [] #holds just the coin names, *includes abbreviations which we want to remove*
    filteredCoins = [] #will hold formatted list of coins

    for css in rawCSS:
        lines += css.text.splitlines() #Split the css into lines

    for line in lines:
        if(line[0] == " " or len(line) == 1): #parse out junk lines
            pass
        else:
            coinNames.append(line) #append coin names/abbreviations into other list

    for coin in range(len(coinNames)):
        if(coin % 2 == 0):
            filteredCoins.append(coinNames[coin]) #coins are followed by their abbreviation so everyother element is a full coin name
    
    return({hedgeName:filteredCoins})

def GrabCoinIcons(coins ,driver):
    for coin in coins:
        print(coin.name)
        url = "https://www.messari.io/asset/"
        name = coin.name
        if ":" in name:
            continue

        url = url + name.replace(" ", '-')

        if exists("icons/{}.png".format(name)) == False:
            driver.implicitly_wait(5)
            element = None
            while not element:
                try:
                    driver.get(url)
                    if(driver.find_element(By.XPATH, "//*[@class = 'MuiAvatar-img css-1hy9t21 e1de0imv0']")):
                        with open('icons/{}.png'.format(name), 'wb') as file:
                            element = driver.find_element(By.XPATH, "//*[@class = 'MuiAvatar-img css-1hy9t21 e1de0imv0']")
                            img = requests.get(element.get_attribute('src')).content
                            file.write(img)
                except:
                    time.sleep(2)
    return True
        
