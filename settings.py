# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SLACK= os.environ.get("SLACK_API_KEY")
OPEN_WEATHER= os.environ.get("OPEN_WEATHER_MAP")
