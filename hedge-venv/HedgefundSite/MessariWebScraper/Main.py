from asyncio.windows_events import NULL
from genericpath import exists
from email.errors import HeaderDefect
from MessariWebScraper import MessariWebScraper as MWS
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from operator import itemgetter, attrgetter
import json, os

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"   #Do not wait for full page load
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors') #ignore SSL cert errors

websites = []  #reads our text file containing the urls of each hedgefund on messari.io
with open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/HedgefundSite/MessariWebScraper/links.txt', 'r') as f:
        websites = f.readlines()
        f.close()

class Coin:
    name = ""
    count = 0
    icon = None

    def __init__(self, name, count, icon):
        self.name = name
        self.count = count
        self.icon = icon

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

    @staticmethod
    def fromJSON(json_dict):
        return Coin(json_dict['name'],
                    json_dict['count'],
                    json_dict['icon'])

def ScrapeNewData(): #scrapes the messari.io website for hedgefunds and their holdings
    hedgefunds = {}

    driver = webdriver.Chrome(chrome_options=options,desired_capabilities=caps, executable_path="C:/WebDrivers/bin/chromedriver.exe")

    for site in websites:
        hedgefunds.update(MWS.GrabMessariData(site, driver))

    driver.quit()

    f = open("json/hedgeCoinData.json", "w")
    json.dump(hedgefunds, f, indent = "")
    return hedgefunds

def ReadExistingData(): #reads a JSON file containing info on hedgefunds and their holdings
    f = open('C:/Users/jared/Desktop/GitHub/HedgefundDjangoServer/HedgefundCryptoAnalyzer/hedge-venv/HedgefundSite/json/hedgeCoinData.json', 'r')
    jsonData = json.load(f)
    return jsonData

def TallyCoins(hedgeDict): #takes raw data of hedgefunds and their holdings and tallies how many hedgefunds hold an individual coin
    coinCount = {}
    for hedge,coinList in hedgeDict.items():
        for coin in coinList:
            if(coin in coinCount):
                coinCount.update({coin: coinCount[coin] + 1})
            else:
                coinCount.update({coin: 1})

    sortedCoins = []
    for coin,count in coinCount.items():
        currCoin = Coin(coin, count, None)
        sortedCoins.append(currCoin)

    sortedCoins = sorted(sortedCoins, key=attrgetter('count'), reverse=True)
    
    return sortedCoins

def GrabIcons(coins):
    driver = webdriver.Chrome(desired_capabilities=caps, executable_path="C:/WebDrivers/bin/chromedriver.exe")
    coinIcons = MWS.GrabCoinIcons(coins, driver)
    
    for coin in coinIcons:
        f = open("json/coins/{}.json".format(coin.name), "w")
        json.dump(coin.toJSON(), f, indent = "")
    return coinIcons

def GetCoin(coin):
    if exists("icons/{}.png".format(coin)) == True:
        f = open("json/coins/{}.json".format(coin), 'r')
        jsonString = json.load(f)            #string JSON
        jsonDict = json.loads(jsonString)    #JSON dict
        coinObject = Coin.fromJSON(jsonDict) #actual class object
        return coinObject
    else:
        return None

def GetCoins():
    coins = []
    for filename in os.scandir("json/coins"):
        f = open(filename.path, 'r')
        jsonString = json.load(f)            #string JSON
        jsonDict = json.loads(jsonString)    #JSON dict
        coins.append(jsonDict)
        
    print(coins)
    return coins

def migrateImages():
    coins = GetCoins()
    for coin in coins:
        c = Coin.fromJSON(coin)
        
        