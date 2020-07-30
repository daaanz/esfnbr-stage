import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler("wZdsf58Ka2jciAifsd5NDg2y1", "FwbZcX6g9vGbpwLyNejLIHdY9KybOhUdEBHVTvXn6YQpa1MpRY")
auth.set_access_token("1285954782545563649-onwph67OZ10ulwjVO8r7p3CIgSFMnD", "tWeoFkLdvv8qZsYBE4wrooaLpFh331Dalj3AT5S9LtGTY")
api = tweepy.API(auth)

url = 'https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version'

setDelay = 60

res = requests.get(url).json()
stage = res

moduleName = stage['moduleName']
buildDate = stage['buildDate']
branch = stage['branch']
build = stage['build']

while 1:
    res = requests.get(url).json()
    buildNew = res['build']

    print(buildNew)
    if buildNew != build:
        try:
            print('El servidor de espera se ha actualizado...')
            api.update_with_media('assets/status.jpg', 'Se ha actualizado el servidor de espera. (FortniteStage)' + '\n\n' + moduleName + '\n' + branch + ' (' + build + ')' '\n\n' + '[' + buildDate + ']')
            print('Publicado correctamente.')
            build = res['build']
        except:
            print('Error. (1)')
    else:
        print('No se detectan cambios. Buscando de nuevo en 60 segundos...')

    time.sleep(setDelay)




    
