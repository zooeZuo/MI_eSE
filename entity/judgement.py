#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

def type_check(param,string):
    if type(param) == type(u''):
        param = param.encode()
    if string == 'int':
        if not isinstance(param, int):
            return string
    if string == 'hexstring':
        if not isinstance(param, str):
            return string
        else:
            param = param.upper()
            for i in range(0, len(param)):
                if not (('0' <= param[i] <= '9') or ('A' <= param[i] <= 'F')):
                    return string
    if string == 'string':
        if not isinstance(param, str):
            return string

    if string == 'list':
        if not isinstance(param,list):
            return string

    if string == 'object':
        if not isinstance(param,object):
            return string
    return 0
