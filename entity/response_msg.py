#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

MSG = {
    '9000':"成功执行",
    '6200':"无信息提供",
    '6281':"回送的数据可能有错",
    '6282':"文件长度<Le",
    '6283':"选择的文件无效",
    '6284':"FCI 格式与P2 指定的不符",
    '62**':"验证失败，还剩下()次尝试机会",
    '6300':"认证失败",
    '63**':"验证失败，还剩下()次尝试机会",
    '6400': "标志状态位未变",
    '6581': "内存失败",
    '6601': "接收通讯超时",
    '6602': "校验和不对",
    '6603': "当前DF 文件无FCI",
    '6604': "当前DF 下无SF 或KF",
    '6700': "长度错误",
    '6882': "不支持安全报文",
    '6900': "不能处理",
    '6901': "命令不接受（无效状态）",
    '6981': "命令与文件结构不相容",
    '6982': "不满足安全状态",
    '6983': "因卡片密钥被锁拒绝迁出",
    '6984': "未取随机数",
    '6985': "使用条件不满足",
    '6986': "使用条件不满足（未建立钱包文件，圈存金额小于已透支金额,交易计数器达到最大值）",
    '6987': "安全报文数据项丢失",
    '6988': "MAC验证失败",
    '6A80': "数据域参数错误（交易金额超出最大金额限制）",
    '6A81': "功能不支持",
    '6A82': "未找到文件",
    '6A83': "未找到记录",
    '6A85': "文件中存储空间不够",
    '6A86': "参数P1 P2错误",
    '6A87': "Lc与P1-P2不一致",
    '6B00': "参数错误（偏移地址超出了EF）",
    '6C**': "长度错误（Le 错误；xx为实际长度）",
    '6D00': "不支持的指令代码",
    '6E00': "不支持的类：CLA 错",
    '6F00': "数据无效",
    '9301': "金额不足",
    '9302': "MAC 无效",
    '9303': "应用永久锁住",
    '9401': "金额不足",
    '9402': "交易计数器到达最大值",
    '9403': "密钥索引不支持",
    '9406': "所需MAC不可用"

}

DATA = {
    'select':'6F328409A00000000386980701A5259F0801029F0C1E869820007590FFFF82052000B2D0614C800960A720140504201605040914',
    'get_version':'112233445566778899',
    'get_information':'998877665544332211',
    'init_for_load':'00030F980004010020A124BA1D7E073D',
    'credit':'17B8946D',
    'init_update':'',
    'put_key':'310BC706A74588F9A7449000',
    'extraditon':'1612120A00002E090102075A90800960A7F716C6B4905AD5C4D50F2C82170FFC5B7713B2C7D23E9AB1A3F06DD3AC7654112D93EBA7DE4B54AF309BF3F6E72E758AAD122E8EDC78DCC9A09FECB689F77350559A4D1DBBFC98CE',
}

STATUS = {
    '1':'received',
    '2':'sent',
    '3':'expired',
    '4':'canceled',
    '5':'delivered'
}
if __name__=='__main__':

    sw = '9000'
    if sw in MSG.keys():
        print(MSG[sw])

    # for s in STATUS.items():
    #     print(s[1])
    #
    # print(STATUS['1'])