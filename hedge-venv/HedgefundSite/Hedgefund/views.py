import mailbox
from django.shortcuts import render
from django.http import HttpResponse
from MessariWebScraper import Main


# Create your views here.
def index(request):
    Main.ScrapeNewData()
    return HttpResponse("Hello, world. You're at the hedgefund index")

