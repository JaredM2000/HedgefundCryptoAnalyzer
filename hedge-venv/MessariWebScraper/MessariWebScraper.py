import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


    
def GrabMessariData(website, driver):

    driver.get(website)
    driver.implicitly_wait(5)
    time.sleep(1) #depending on load time we get an incorrect web page title, so we sleep, *we want title because it can tell us which hedgefund we are viewing"
    hedgeName = driver.title
    print("Hedgefund: ",hedgeName)

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
        
