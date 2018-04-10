#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/4/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from django.http import HttpResponse, HttpResponseBadRequest
import json
from eSE.models import restrict
import logging

def response_result(req):
    res_data = {
        'resultCode': '0000',
        'reslutMsg': '收到APDU,执行完后,将推送apdu执行结果',
        'xmTransNum': req['xmTransNum'],
        'xmTransTime': req['xmTransTime'],
        'spTransNum': req['spTransNum'],
        'spTransTime': req['spTransTime'],
    }
    logging.debug('收到脚本')
    logging.debug(HttpResponse(res_data))
    return HttpResponse(res_data)

def receive_data(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        if 'apduType' and 'dpanCode' and 'scriptsInstanceId' and 'apduModelList' \
                and 'xmTransNum' and 'xmTransTime' and 'spTransNum' and 'spTransTime' in req:
            logging.debug(req)

            restrict.objects.create(
                apduModelList=req['apduModelList'],
                scriptsInstanceId=req['scriptsInstanceId'],
                xmTransNum=req['xmTransNum'],
                xmTransTime=req['xmTransTime'],
                spTransNum=req['spTransNum'],
                spTransTime=req['spTransTime'],
            )

            return response_result(req)

        else:
            return HttpResponseBadRequest('参数错误！！！')


    else:
        return HttpResponse('要求POST方法')