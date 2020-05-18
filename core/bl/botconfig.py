import json

import vk

from core.bl.keyboard import getKeyboard


class BotConfig():
    def __init__(self):
        session = vk.Session()
        self.api = vk.API(session, v=5.8)
        with open('./json/config.json', "r") as js_file:
            config = json.load(js_file)
            self.token = config['token']
        self.keyboard = getKeyboard()
