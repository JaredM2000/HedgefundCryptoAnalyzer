from asyncio.windows_events import NULL
from email.errors import HeaderDefect
from MessariWebScraper import MessariWebScraper as MWS
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from operator import itemgetter, attrgetter
import json


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')



websites = []
with open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/MessariWebScraper/links.txt', 'r') as f:
        websites = f.readlines()
        f.close()

class Coin:
    name = ""
    count = 0

def ScrapeNewData():
    hedgefunds = {}

    driver = webdriver.Chrome(chrome_options=options,desired_capabilities=caps, executable_path="C:/WebDrivers/bin/chromedriver.exe")

    for site in websites:
        hedgefunds.update(MWS.GrabMessariData(site, driver))

    driver.quit()

    f = open("hedgeCoinData.json", "w")
    json.dump(hedgefunds, f, indent = "")
    return True

def ReadExistingData():
    f = open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/HedgefundSite/hedgeCoinData.json', 'r')
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

def GrabIcons(coins):
    driver = webdriver.Chrome(desired_capabilities=caps, executable_path="C:/WebDrivers/bin/chromedriver.exe")
    coinIcons = MWS.GrabCoinIcons(coins, driver)
    return coinIcons
        



