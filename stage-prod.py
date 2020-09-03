import requests
import tweepy
import time
import os
from os import environ
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO

auth = tweepy.OAuthHandler(environ["CONSUMER_TOKEN"], environ["CONSUMER_SECRET"])
auth.set_access_token(environ["KEY"], environ["SECRET"])
api = tweepy.API(auth)

def download_img(url, file_name):
        r = requests.get(url)
        im = Image.open(BytesIO(r.content))
        im.save('assets.png')

url_stage = 'https://fortnite-public-service-stage.ol.epicgames.com/fortnite/api/version'
response_stage = requests.get(url_stage).json()
versionOld = response_stage['version']
setDelay = 60

while 1:
    stage_res_new = requests.get(url_stage).json()
    versionNew = stage_res_new['version']
    buildNew = stage_res_new['build']
    if versionNew != versionOld:
        print('Change in Stage.')
        print(versionNew)
        branch = stage_res_new['branch']
        img_url = 'https://esfnbr.com/content/images/assets.png'
        file = ('assets.png')
        download_img(img_url, file)
        api.update_with_media('assets.png', 'Se ha añadido el Parche ' + versionNew + ' (' + buildNew + ') ' + 'al servidor de espera (FortniteStage)' + '\n\n' + 'Debería lanzarse en los próximos días.')
        versionOld = stage_res_new['version']
    else:
        print('No change in Stage.')
    
    time.sleep(setDelay)




    
