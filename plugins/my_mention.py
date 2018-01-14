from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime import datetime
from pygeocoder import Geocoder
import urllib.request
import json
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()

 # load up the entries as environment variables
load_dotenv(dotenv_path)

token = os.environ.get("OPEN_WEATHER_MAP")


@respond_to('時間')
def mention_func(message):
    message.reply("今の時間は")
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message.send(now)
    message.send("だぞ")

@listen_to('お腹減った')
def listen_func(message):
    message.reply('二郎に行ってみてはどうかね？')

@listen_to('(.*)の天気')
def return_weather(message, place):
    message.reply('{}の天気は'.format(place))
    results = Geocoder.geocode(place)
    place_list = results[0].coordinates
    #1st is lat 2nd is lon
    mode = "json"
    metric = "Metric"
    lat = place_list[0]
    lon = place_list[1]
    appid = token
    url = "http://api.openweathermap.org/data/2.5/weather?lat={a}&lon={b}&units={c}&appid={d}".format(a=lat, b=lon, c=metric, d=appid)
    response = urllib.request.urlopen(url).readline()
    weather = json.loads(response.decode('utf-8'))
    message.reply("天気は" + str(weather['weather'][0]['description']) + "で")
    message.send("気温は" + str(weather['main']['temp']) + "度だぞ")
