import json

from core.bl.botconfig import BotConfig


def getVkUser(uid, api, token):
    return api.users.get(access_token=token, user_ids=uid)


class Messages:
    def __init__(self):
        cnf = BotConfig()
        self.token = cnf.token
        # self.keyboard = cnf.keyboard
        self.api = cnf.api

    def sendPdfToUser(self, attach, uid):
        try:
            self.api.messages.send(access_token=self.token, user_id=uid, attachment=attach, )
        except:
            return False

    def sendMessage(self, message, uid):
        self.api.messages.send(access_token=self.token, user_id=uid, message=message, )

    def sendmsg(self, msg):
        pass

    def sendSuccess(self):
        pass

    def sendError(self, uid):
        self.api.messages.send(access_token=self.token, user_id=uid, message="я не понимаю", )
