""" Send Ombi Movie Requests to RSSCrawler, needs working pyjq and requests packages. Please do "pip install pyjq" and "pip install requests" """
import json
import secrets

import pyjq
import requests

OmbiUrl=secrets.OmbiUrl  
OmbiApi=secrets.OmbiApi  
tMDbApiKey=secrets.tMDbApiKey
RSScrawlerURL=secrets.RSScrawlerURL

#fragt am Ombi-Server nach Anfragen, erhält eine Liste wobei jedes Element wie fogt aufgebaut ist (Id der Anfrage, tmdb, Genehmigung)
def GetOmbiRequests(Url,Api):
    movies=requests.get(Url+'/api/v1/Request/movie', headers={'ApiKey': Api})
    movies=movies.json()
    OmbiRequests=pyjq.all('.[] | [.id, .theMovieDbId, .approved]', movies)
    return OmbiRequests

#prüft ob Anfrage genehmigt, ansonsten wird der Wunsch aus der Liste entfernt
def CheckApprovalStatus(ombiList):
    ombiList=[i for i in ombiList if i[2]!=False]
    return ombiList
    
# Ersetzt die tmdb-id durch den deutschen Titel 
def GetGermanTitle(movieList,Api):
    for i in movieList:
      germanTitle=requests.get('https://api.themoviedb.org/3/movie/'+format(i[1])+'?api_key='+Api+'&language=de-DE',headers={'Content-Type':'application/json'})
      germanTitle=germanTitle.json()
      germanTitle=pyjq.all('. | .title', germanTitle)
      i[1] = germanTitle.pop()
    return movieList

#Sendet die deutschen Titel an die RSScrawler-Api und löscht bei Erfolg die Anfrage auf Ombi-Server
def SendMovieToRSScrawler(movieList,RSScrawlerURL):
    for i in movieList:
        rss_request=requests.post(RSScrawlerURL+"/api/download_movie/"+format(i[1]))
        if rss_request.ok == True:
            requests.delete(OmbiUrl+"/api/v1/Request/movie/"+format(i[0]), headers={'ApiKey': OmbiApi})
    return movieList


def main():
    ombiList=GetOmbiRequests(OmbiUrl,OmbiApi)
    approvedList=CheckApprovalStatus(ombiList)
    germanTitle=GetGermanTitle(approvedList,tMDbApiKey)
    SendMovieToRSScrawler(germanTitle,RSScrawlerURL)
   
main()
