import requests
import os
import json
from PIL import Image

def get_picture_of_the_day():
  url = "https://api.nasa.gov/planetary/apod?api_key={}".format(os.getenv('api_key'))
  response = requests.get(url)
  print(response.status_code)
  if not response.status_code == 200:
   return 0
  print(response.text)
  data = json.loads(response.text)
  hdurl = data.get('hdurl', "")
  explanation = data.get('explanation', "")
  return hdurl, explanation
