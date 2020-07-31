import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler(environ["CONSUMER_TOKEN"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["KEY"], environ["SECRET"])
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




    
