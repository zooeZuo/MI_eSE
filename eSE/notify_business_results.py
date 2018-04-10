#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from django.http import HttpResponse,HttpResponseBadRequest
import json
import requests
from eSE.models import restrict


url = 'http://192.168.39.110:8080/SHSRC/TSM/1/1/NotifyBusinessResults'
headers = {'Content-type': 'application/json;charset=UTF-8'}

def response_data(req):
    res = {
        "resultCode": "0000",
        "resultMsg": "SUCCESS",
        "xmTransTime": req["xmTransTime"],
        "xmTransNum": req["xmTransNum"],
        "spTransTime": req["spTransTime"],
        "spTransNum": req["spTransNum"],
    }
    return HttpResponse(res)

def receive_data(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        if req.has_key('deviceInfo') and req.has_key('dpanCode')\
                and req.has_key('authenticationCode') and req.has_key('xmTransTime')\
                and req.has_key('xmTransNum'):
            restrict.objects.create(
                xmTransTime=req["xmTransTime"],
                xmTransNum=req["xmTransNum"],
                spTransTime=req["spTransTime"],
                spTransNum=req["spTransNum"],
            )

            return response_data(req)

        else:
            return HttpResponseBadRequest('请求数据不正确')