import requests
import tweepy
import time
import os
from os import environ

auth = tweepy.OAuthHandler(environ["CONSUMER_TOKEN"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["KEY"], environ["SECRET"])
api = tweepy.API(auth)

url_stage = 'https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version'
url_live = 'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/version'

setDelay = 60

# Stage
res_stage = requests.get(url_stage).json()
stage = res_stage

# Live
res_live = requests.get(url_live).json()
live = res_live

# Stage Variables
build = stage['build']

# Live Variables
build_live = live['build']

# General Loop
while 1:
    # Diff. Stage
    res_stage_new = requests.get(url_stage).json()
    buildNew = res_stage_new['build']
    if buildNew != build:
        try:
            # Stage Variables
            moduleName = res_stage_new['moduleName']
            buildDate = res_stage_new['buildDate']
            branch = res_stage_new['branch']
            build = res_stage_new['build']
            print('El servidor de espera se ha actualizado... (FortniteStage)')
            api.update_status('Se ha actualizado el servidor de espera. (FortniteStage)' + '\n\n' + moduleName + '\n' + branch + ' (' + build + ')' '\n\n' + '[' + buildDate + ']')
            print('Publicado correctamente en Twitter. (FortniteStage)')
            build = res_stage_new['build']
        except:
            print('Error. (1-FortniteStage)')
    else:
        print('No se detectan cambios. Buscando de nuevo en 60 segundos... (FortniteStage)')
    
    # Diff. Live
    res_live_new = requests.get(url_live).json()
    buildNew_live = res_live_new['build']
    if buildNew_live != build_live:
        try:
            # Live Variables
            moduleName_live = res_live_new['moduleName']
            buildDate_live = res_live_new['buildDate']
            branch_live = res_live_new['branch']
            build_live = res_live_new['build']
            print('El servidor de Fortnite se ha actualizado... (FortniteLive)')
            api.update_status('Se ha actualizado el servidor de Fortnite. (FortniteLive)' + '\n\n' + moduleName_live + '\n' + branch_live + ' (' + build_live + ')' '\n\n' + '[' + buildDate + ']')
            print('Publicado correctamente en Twitter. (FortniteLive)')
            build_live = res_live_new['build']
        except:
            print('Error. (1-FortniteLive)')
    else:
        print('No se detectan cambios. Buscando de nuevo en 60 segundos... (FortniteLive)')

    time.sleep(setDelay)





    
