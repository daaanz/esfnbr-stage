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

url_stage = 'https://esfnbr.com/content/images/stage.json'
response_stage = requests.get(url_stage).json()
buildOld = response_stage['build']
setDelay = 60

while 1:
    stage_res_new = requests.get(url_stage).json()
    buildNew = stage_res_new['build']
    if buildNew != buildOld:
        print('Change in Stage.')
        print(buildNew)
        branch = stage_res_new['branch']
        img_url = 'https://esfnbr.com/content/images/assets.png'
        file = ('assets.png')
        download_img(img_url, file)
        api.update_with_media('assets.png', 'Se ha actualizado el servidor de espera (FortniteStage)' + '\n\n' + branch + ' (' + buildNew + ')')
    else:
        print('No change in Stage.')
    
    time.sleep(setDelay)




    
