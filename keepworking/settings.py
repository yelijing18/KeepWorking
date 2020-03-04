# -*- coding: utf-8 -*-

from decouple import config
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env', usecwd=True))
load_dotenv(find_dotenv('default.env', raise_error_if_not_found=True))

COUNTDOWN = config('COUNTDOWN', default=5, cast=int)
EVENT_INTERVAL = config('EVENT_INTERVAL', default=1, cast=int)
