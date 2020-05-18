import json
import threading

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from core.requestProcessing import rowToData


@csrf_exempt
def pdfConvertorHome(request):
    rq = json.loads(request.body, encoding="utf-8")

    if rq['type'] != "confirmation":
        x = threading.Thread(target=rowToData, args=(request,))
        x.start()
        # rowToData(request)
        return HttpResponse("ok", status=200)
    else: return HttpResponse("fc8047cf")
