#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7453205223:AAGjZ03nRAntwbCw1rDd_4KYllr5lE-3uaw")
    API_ID = int(os.environ.get("API_ID", "18156248"))
    API_HASH = os.environ.get("API_HASH", "db946fb6805b1a698c679626b617e77a")
    AUTH_USERS = os.environ.get("AUTH_USERS", "2032347579")
