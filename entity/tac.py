#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'


def TAC_enc(keys, datas):
    assert len(keys) == 32
    assert len(datas) == 48

    length = len(keys) / 2
    first_half_key = keys[:length]
    second_half_key = keys[length:]

    tac_1 = ord(first_half_key) ^ ord(datas)
    tac_2 = ord(tac_1) ^ ord(second_half_key)

    return tac_2


if __name__ == '__main__':
    key = '11223344556677889900112233445566'
    data = '12165464688448486764846846454864634123554554468'
    TAC_enc(key,data)
