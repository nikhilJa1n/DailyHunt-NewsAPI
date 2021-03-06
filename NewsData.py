#Coded By Gowtham on 30/05/2020 
#Coded Using Vim Text Editor
import requests
import json
from bs4 import BeautifulSoup as bs
from genUrl import getUrl


def paraParse(newsContent):
    soup = bs(newsContent, "lxml")
    pTags = soup.findAll("p")
    cont = ""
    for i in range(len(pTags)):
        singleTag = pTags[i].text
        cont = cont + singleTag + "\n"
    return cont.strip()


def newsData(query):
    newsDictionary = {
        'success': True,
        'data': []
    }
    URL = getUrl(query)
    r = requests.get(URL)

    responseDict = json.loads(r.content)
    datasDict = responseDict["data"]

    rows = datasDict["rows"]

    content = ""

    for row in rows:
        try:
            title = row["title"]
        except:
            title = ""
        try:
            url = row["shareUrl"]
        except:
            url = ""
        try:
            contentImage = row["contentImage"]
        except:
            contentImage = ""
        try:
            ImageUrl = contentImage["url"]
        except:
            ImageUrl = ""
        try:
            counter = row["counter"]
        except:
            counter = ""
        try:
            PublishedDt = counter["ingestionDate"]
        except:
            PublishedDt = ""
        try:
            viewCount = counter["viewsCount"]
        except:
            viewCount = ""
        try:
            newsContent = row["content"]
            content = paraParse(newsContent)
        except:
            newsContent = ""
        try:
            publisherStory = row["publisherStoryUrl"]
        except:
            publisherStory = ""
        newsObject = {
            'title': title,
            'imageUrl': ImageUrl,
            'url': url,
            'content': content,
            'PublishedTime': PublishedDt,
            'viewCount': viewCount,
            'publisherStory': publisherStory
        }

        newsDictionary['data'].append(newsObject)

    return newsDictionary
