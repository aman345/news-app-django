from django.shortcuts import render
from newsapi import NewsApiClient
import logging

def index(request):
    newsapi: NewsApiClient = NewsApiClient(api_key="YOUR_API_KEY")
    top = newsapi.get_everything(sources="bbc-news",language='en')
    logging.debug("News Returned From", top)

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request,'index.html',context={'mylist':mylist})
