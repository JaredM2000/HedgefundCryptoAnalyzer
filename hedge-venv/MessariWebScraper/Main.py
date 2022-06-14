from asyncio.windows_events import NULL
from email.errors import HeaderDefect
from MessariWebScraper import MessariWebScraper as MWS
from selenium import webdriver
from selenium.webdriver.common.by import By
from operator import itemgetter, attrgetter
import json

websites = []
with open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/MessariWebScraper/links.txt', 'r') as f:
        websites = f.readlines()
        f.close()

class Coin:
    name = ""
    count = 0

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
    f = open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/MessariWebScraper/data.json', 'r')
    jsonData = json.load(f)
    return jsonData

def TallyCoins(hedgeDict):
    coinCount = {}
    for hedge,coinList in hedgeDict.items():
        for coin in coinList:
            if(coin in coinCount):
                coinCount.update({coin: coinCount[coin] + 1})
            else:
                coinCount.update({coin: 1})

    sortedCoins = []
    for coin,count in coinCount.items():
        currCoin = Coin()
        currCoin.name = coin
        currCoin.count = count
        sortedCoins.append(currCoin)
    
    return sorted(sortedCoins, key=attrgetter('count'), reverse=True)

        



