#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'

from entity.response import RAPDU
from entity.log import logger
from entity.response_msg import DATA
from entity import nonce
#from scp02_channel import send_apdu
from entity.response_msg import MSG

# 随机数
challenges_4 = nonce.Serial_4()
challenges_8 = nonce.Terminal_Generator_8()
challenges_10 = nonce.Terminal_Generator_10()

class CAPDU(object):

    COMMANDS = {
        #通用指令
        'SelectFile':[0x00, 0xA4],#选择文件
        'GetApplicationVersion':[0x80,0x0A],#获取应用版本信息
        'StoreData':[0x84,0xE2] or [0x80,0xE2],#写入数据
        'Install': [0x84, 0xE6] or [0x80,0xE6],  # 安装
        'Load':[0x84,0xE8] or [0x80,0xE8],# 加载
        'ManageChannel':[0x00,0x70],# 管理通道
        'PutKey':[0x84,0xD8] or [0x80,0xD8],# 密钥
        'SetStatus':[0x84,0xF0] or [0x80,0xF0],# 设置状态
        'GetStatus':[0x84,0xF2] or [0x80,0xF2],# 取得状态
        'GetData':[0x00,0xCA] or [0x80,0xCA] or [0x84,0xCA],# 取数据
        'ExternalAuth':[0x84,0x82], # 外部认证
        'InternalAuth':[0x84,0x88], # 内部认证
        #个人化阶段指令
        'GetChallenge':[0x00,0x84],#取随机数
        'GetApplicationInformation':[0x00,0x0A],#获取应用版本信息
        'InitializeForLoad':[0x80,0x50],# 圈存初始化 或 初始化更新
        'CreditForLoad':[0x80,0x52],#圈存命令
        'Extradition':[0x84,0xBE]#应用迁出指令
    }



    def apdu_type_check(self,apdu):
        from smartcard.util import toHexString
        select = str(toHexString(self.COMMANDS['SelectFile'])).replace(' ','')
        version = str(toHexString(self.COMMANDS['GetApplicationVersion'])).replace(' ','')
        store_data = str(toHexString(self.COMMANDS['StoreData'])).replace(' ','')
        install = str(toHexString(self.COMMANDS['Install'])).replace(' ','')
        load = str(toHexString(self.COMMANDS['Load'])).replace(' ','')
        channel = str(toHexString(self.COMMANDS['ManageChannel'])).replace(' ','')
        put_key = str(toHexString(self.COMMANDS['PutKey'])).replace(' ','')
        set_status = str(toHexString(self.COMMANDS['SetStatus'])).replace(' ','')
        get_status = str(toHexString(self.COMMANDS['GetStatus'])).replace(' ','')
        get_data = str(toHexString(self.COMMANDS['GetData'])).replace(' ','')
        challenge = str(toHexString(self.COMMANDS['GetChallenge'])).replace(' ','')
        info = str(toHexString(self.COMMANDS['GetApplicationInformation'])).replace(' ','')
        initialize = str(toHexString(self.COMMANDS['InitializeForLoad'])).replace(' ','')
        credit = str(toHexString(self.COMMANDS['CreditForLoad'])).replace(' ','')
        extradition = str(toHexString(self.COMMANDS['Extradition'])).replace(' ','')
        ex_auth = str(toHexString(self.COMMANDS['ExternalAuth'])).replace(' ','')
        in_auth = str(toHexString(self.COMMANDS['InternalAuth'])).replace(' ','')

        length = len(apdu[10:]) / 2
        data_len = int(apdu[8:10].upper(), 16)
        cut_line = '-'*60
        rapdu = RAPDU()

        # 指令类型判断
        if apdu[:4] == select:
            logger.debug(cut_line)
            logger.debug('Select File')
            logger.debug('<-APDU req: '+apdu)

            if apdu[4:8] == '0400':
                assert 10 <= length <= 32
                logger.debug('Select by AID')
                # 判断数据长度
                if data_len == length:
                    logger.debug('->APDU res: ' + DATA['select'] + rapdu.SuccessResponse())
                    logger.debug(MSG['9000'])
                    return DATA['select'] + rapdu.SuccessResponse()
                else:
                    sw = '6C**'
                    msg = MSG[sw]
                    logger.debug('->APDU res: ' + sw)
                    logger.debug(msg)
                    return sw

            elif apdu[4:8] == '0000':
                assert length == 4
                logger.debug('Select by FID')

                # 判断数据长度
                if data_len == length:
                    logger.debug('->APDU res: '+DATA['select']+rapdu.SuccessResponse())
                    logger.debug(MSG['9000'])
                    return DATA['select']+rapdu.SuccessResponse()
                else:
                    sw = '6C**'
                    msg = MSG[sw]
                    logger.debug('->APDU res: ' + sw)
                    logger.debug(msg)
                    return sw

            else:
                sw = '6A86'
                msg = MSG[sw]
                logger.debug('->APDU res: ' + sw)
                logger.debug('{0}' + msg)

                return sw

        elif apdu[:4] == version:
            logger.debug(cut_line)
            logger.debug('Get Application Version')
            logger.debug('<-APDU req: ' + apdu)
            if apdu[4:8] == '0001' or '0080':
                logger.debug('获取内部版本')
                logger.debug('->APDU res: ' + DATA['get_version'] + rapdu.SuccessResponse())
            elif apdu[4:8] == '0002':
                logger.debug('获取外部版本')
                logger.debug('->APDU res: ' + DATA['get_version'] + rapdu.SuccessResponse())

            return DATA['get_version'] + rapdu.SuccessResponse()

        elif apdu[:4] == store_data:
            logger.debug(cut_line)
            logger.debug('Store Data')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                sw = '6C**'
                msg = MSG[sw]
                logger.debug('->APDU res: ' + sw)
                logger.debug(msg)

                return sw

        elif apdu[:4] == install:
            logger.debug(cut_line)
            logger.debug('Install')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                sw = '6C**'
                msg = MSG[sw]
                logger.debug('->APDU res: ' + sw)
                logger.debug(msg)

                return sw

        elif apdu[:4] == load:
            logger.debug(cut_line)
            logger.debug('Load')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == channel:
            logger.debug(cut_line)
            logger.debug('Manage Channel')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())

                return rapdu.ErrorResponse()

        elif apdu[:4] == put_key:
            logger.debug(cut_line)
            logger.debug('Put Key')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' +DATA['put_key']+ rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())

                return rapdu.ErrorResponse()

        elif apdu[:4] == set_status:
            logger.debug(cut_line)
            logger.debug('Set Status')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())

                return rapdu.ErrorResponse()

        elif apdu[:4] == get_status:
            logger.debug(cut_line)
            logger.debug('Get Status')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == get_data:
            logger.debug(cut_line)
            logger.debug('Get Data')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == challenge:
            logger.debug(cut_line)
            logger.debug('Get Challenge')
            logger.debug('<-APDU req: ' + apdu)

            if apdu[-2:] == '04':
                logger.debug('->APDU res: ' +challenges_4+rapdu.SuccessResponse())
                return challenges_4+rapdu.SuccessResponse()
            elif apdu[-2:] == '08':
                logger.debug('->APDU res: ' +challenges_8+rapdu.SuccessResponse())
                return challenges_8 + rapdu.SuccessResponse()
            elif apdu[-2:] == '0A':
                logger.debug('->APDU res: ' + challenges_10 + rapdu.SuccessResponse())
                return challenges_10 + rapdu.SuccessResponse()
            else:
                sw = '6C**'
                msg = MSG[sw]
                logger.debug('->APDU res: ' + sw)
                logger.debug(msg)

                return sw

        elif apdu[:4] == info:
            logger.debug(cut_line)
            logger.debug('Get Application Information')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' +DATA['get_information']+rapdu.SuccessResponse())
                return DATA['get_information']+rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == initialize and apdu[4:6] == '00':
            logger.debug(cut_line)
            logger.debug('Initialize For Load')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' +DATA['init_for_load']+rapdu.SuccessResponse())
                return DATA['init_for_load']+rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[0:4] == initialize and apdu[4:6] == '20':
            logger.debug(cut_line)
            logger.debug('Initialize Update')
            logger.debug('<-APDU req: ' + apdu)
            lengths = len(apdu[10:-2])/2
            if data_len == lengths:
                logger.debug('->APDU res: ' + DATA['init_update'] + rapdu.SuccessResponse())
                return DATA['init_update'] + rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()


        elif apdu[:4] == credit:
            logger.debug(cut_line)
            logger.debug('Credit For Load')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + DATA['credit'] + rapdu.SuccessResponse())
                return DATA['credit'] + rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == extradition:
            logger.debug(cut_line)
            logger.debug('Extradition')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + DATA['extraditon'] + rapdu.SuccessResponse())
                return DATA['extraditon'] + rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == ex_auth:
            logger.debug(cut_line)
            logger.debug('External Authenticate')
            logger.debug('<-APDU req: ' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        elif apdu[:4] == in_auth:
            logger.debug(cut_line)
            logger.debug('Internal Authenticate')
            logger.debug('<-APDU req：' + apdu)
            if data_len == length:
                logger.debug('->APDU res: ' + rapdu.SuccessResponse())
                return rapdu.SuccessResponse()
            else:
                logger.debug('->APDU res: ' + rapdu.ErrorResponse())
                return rapdu.ErrorResponse()

        else:
            logger.debug('没有该类型的APDU指令！！！')



if __name__=='__main__':
    obj = CAPDU()
    s = obj.apdu_type_check('00A404000BA0000003464D534854534D')
    print(s)
    i = obj.apdu_type_check('805020000861763E10DD444246')
    print(i)