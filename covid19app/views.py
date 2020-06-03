from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests,json


# Create your views here.
def index(request):
    return render(request,'index.html')

def urgent(request):
    return render(request,'urgent.html')

def techstack(request):
    return render(request,'techstack.html')

def trackingtable(request):
    return render(request,'trackingtable.html')

def getnews(request):
    try:
        q = "coronavirus cases"
        urlpart1 = "https://newsapi.org/v2/everything?q="
        urlpart2 = "&sortBy=publishedAt&pageSize=12&language=en&apiKey="
        API_KEY = "09ea697cc4764ec0ab4987df2ad097fc"
        main_url = urlpart1+str(q)+urlpart2+API_KEY
        # fetching data in json format
        page = requests.get(main_url).json()
        # getting all articles in a string article
        articles = page["articles"]
        mydict = {
            "error":False,
            "result":True,
            "keyword":q,
            "articles":articles
        }
        return render(request,'news.html',context=mydict)
    except:
        mydict = {
            "error":True,
            "result":False
        }
        return render(request,'news.html',context=mydict)