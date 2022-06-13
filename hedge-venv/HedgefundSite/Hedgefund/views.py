import mailbox
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from MessariWebScraper import Main


# Create your views here.
def index(request):
    data = Main.ReadExistingData()
    return JsonResponse(data)

def new(request):
    #Main.ScrapeNewData()
    return HttpResponse("hello")

