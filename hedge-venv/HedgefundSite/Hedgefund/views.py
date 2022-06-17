import mailbox
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from MessariWebScraper import Main
import json


# Create your views here.
def index(request):
    data = Main.ReadExistingData()
    return JsonResponse(data)

def new(request):
    Main.ScrapeNewData()
    return HttpResponse("New Data has been scraped")

def icons(request):
    hedgeData = Main.ReadExistingData()
    coinData = Main.TallyCoins(hedgeData)

    Main.GrabIcons(coinData)
    return HttpResponse("Coin icons added")

def test(request):
    hedgeData = Main.ReadExistingData()
    coinData = Main.TallyCoins(hedgeData)

    countList = []
    coinList = []
    for coin in coinData:
        if(coin.count > 1):
            coinList.append(coin.name)
            countList.append(coin.count)

    print(coinList)
    print(countList)

    context = { 'coin_name' : json.dumps(coinList),
                'coin_count': json.dumps(countList) }

    return render(request, 'hedgefund/index.html', context)

def test2(request):
    coin = Main.getCoinInfo("Bitcoin")

    return JsonResponse(coin, safe= False)

