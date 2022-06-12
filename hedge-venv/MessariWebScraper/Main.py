from MessariWebScraper import MessariWebScraper as MWS
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

websites = []
with open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/hedge-venv/MessariWebScraper/links.txt', 'r') as f:
        websites = f.readlines()
        f.close()

def ScrapeNewData():
    hedgefunds = {}

    driver = webdriver.Chrome()

    for site in websites:
        hedgefunds.update(MWS.GrabMessariData(site, driver))

    for key in hedgefunds:
        
        print(key, hedgefunds[key])

    driver.quit()
    return hedgefunds

def ReadExistingData():
    return
