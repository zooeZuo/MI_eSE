#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from django.http import HttpResponse,HttpResponseBadRequest
import json
from eSE.models import restrict
from entity.response_msg import STATUS

def response_data(req):
    res = {
        "resultCode": "0000",
        "resultMsg": "SUCCESS",
        "scriptsStatus":STATUS['1'],
        "xmTransTime": req["xmTransTime"],
        "xmTransNum": req["xmTransNum"],
        "spTransTime": req["spTransTime"],
        "spTransNum": req["spTransNum"],
    }
    return HttpResponse(res)

def receive_data(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        if req.has_key('scriptsInstanceId') and req.has_key('spTransTime')\
                and req.has_key('spTransNum'):
            print(req)
            restrict.objects.create(
                xmTransTime=req["xmTransTime"],
                xmTransNum=req["xmTransNum"],
                spTransTime=req["spTransTime"],
                spTransNum=req["spTransNum"],
            )

            return response_data(req)

        else:
            return HttpResponseBadRequest('请求数据不正确')