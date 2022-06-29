import mailbox
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from MessariWebScraper import Main
from django.core.serializers.json import DjangoJSONEncoder
import json

class JsonEncoder (DjangoJSONEncoder):
    def default (self, obj):
        if callable(getattr(obj, "toJSON", None)):
            return obj.toJSON()

        return super(obj)

# Create your views here.
def index(request):
    data = Main.ReadExistingData()
    return JsonResponse(data)

def new(request):
    Main.ScrapeNewData()
    return HttpResponse("New Data has been scraped")

def old(request):
    response = Main.ReadExistingData()
    return JsonResponse(response)

def getCoins(request):
    coins = Main.GetCoins()

    return JsonResponse(coins, safe=False)

def getCoin(request):
    coinName = request.GET.get("coin", "")
    coinInfo = Main.GetCoin(coinName)

    return JsonResponse(coinInfo, encoder=JsonEncoder, safe=False)

def icons(request):
    hedgeData = Main.ReadExistingData()
    coinData = Main.TallyCoins(hedgeData)

    Main.GrabIcons(coinData)
    return HttpResponse("Coin icons added")

def test(request):
    

    context = {

    }
    return render(request, 'hedgefund/index.html', context)

def test2(request):
    coin = Main.getCoin("Bitcoin")
    return JsonResponse(coin, encoder=JsonEncoder, safe=False)

