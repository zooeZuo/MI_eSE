#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import random

class RAPDU(object):


    @staticmethod
    def SuccessResponse():
        """ success result code"""
        sw = '9000'

        return sw


    @staticmethod
    def WarningResponse():
        """warning result code"""
        WARNING = ['6200','6281','6282','6283','6284','6300',]
        #for i in range(0,len(WARNING)):
        #sw = WARNING[i]

        length = len(WARNING)
        i = random.randint(0,length-1)
        sw = WARNING[i]
        return sw


    @staticmethod
    def ErrorResponse():
        ERROR = [
            '6400','6581','6601',
            '6602','6603','6604',
            '6700','6882',
            '6900','6901','6981','6982','6983','6984','6985','6986','6987',
            '6A80','6A81','6A82','6A83','6A84','6A86','6A87',
            '6B00','6C**','6D00','6E00','6F00',
            '9301','9302','9303',
            '9401','9402','9403','9406',
        ]

        length = len(ERROR)
        i = random.randint(0, length - 1)
        sw = ERROR[i]
        return sw


if __name__=='__main__':
    obj1 = RAPDU.SuccessResponse()
    obj2 = RAPDU.WarningResponse()
    obj3 = RAPDU.ErrorResponse()
    s = obj1
    print(s)
    w = obj2
    print(w)
    e = obj3
    print(e)