#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
from django.http import HttpResponse, HttpResponseBadRequest
import json
import requests
from entity.command import CAPDU
from eSE.models import restrict
from smart_card import Card
from entity.log import logger
from smart_card.Card import CheckIf

url = 'http://192.168.39.110:7001/SHSRC/MI/TSM/1/1/PostApduResults'
headers = {'Content-type': 'application/json;charset=UTF-8'}


def receive_data(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        if 'apduType' and 'dpanCode' and 'scriptsInstanceId' and 'apduModelList' \
                and 'xmTransNum' and 'xmTransTime' and 'spTransNum' and 'spTransTime' in req:
            print(req)
            card = Card.Card('Remote')
            try:
                apduResultList = []
                apdus = req['apduModelList']
                # length = len(apdus)
                count = 0
                for cmd in apdus:
                    count = count + 1
                    print(count)
                    apdu = cmd['apdu']
                    # logger.debug('-> APDU: ',apdu)
                    print(apdu)
                    # card.Reset()
                    res, sw = card.Transmit(apdu)
                    # logger.debug('<- APDU: ',(res + sw))
                    # logger.debug('*' * 60)
                    # CheckIf(sw == '9000', sw)

                    capdu = CAPDU()
                    res_cmd = capdu.apdu_type_check(apdu)

                    # 将相应指令添加进列表
                    apduResultList.append({'reSPonseData': res, 'status': sw})
                    # apduResultList.append({'reSPonseData': res_cmd[:-4], 'status': res_cmd[-4:]})


            except Exception as e:
                print('处理异常', e)

            restrict.objects.create(
                apduResultList=apduResultList,
                apduModelList=req['apduModelList'],
                scriptsInstanceId=req['scriptsInstanceId'],
                xmTransNum=req['xmTransNum'],
                xmTransTime=req['xmTransTime'],
                spTransNum=req['spTransNum'],
                spTransTime=req['spTransTime'],
            )

            res_data = {
                'resultCode': '0000',
                'reslutMsg': '收到APDU,执行完后,将推送apdu执行结果',
                'xmTransNum': req['xmTransNum'],
                'xmTransTime': req['xmTransTime'],
                'spTransNum': req['spTransNum'],
                'spTransTime': req['spTransTime'],
            }
            data = {
                'result': 'SUCCESS',
                'apduResultList': apduResultList,
                'scriptsInstanceId': req['scriptsInstanceId'],
                'xmTransNum': req['xmTransNum'],
                'xmTransTime': req['xmTransTime'],
                'spTransNum': req['spTransNum'],
                'spTransTime': req['spTransTime'],
            }
            # datas = json.dumps(data)
            # res = requests.post(url, data=datas, headers=headers)
            # print(res.content)
            card.Close()
            print('脚本响应',res_data)
            return HttpResponse(res_data)


    else:
        return HttpResponseBadRequest('请求有误！！！')
