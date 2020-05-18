import json

from jconfig import Config

from core.bl.botconfig import BotConfig
from core.bl.sendMessage import Messages
from pdfConwerter.main import Router


def rowToData(request):
    rq = json.loads(request.body, encoding="utf-8")
    if rq['type'] == "message_new":
        body = rq["object"]
        Router(body['message']["id"])
