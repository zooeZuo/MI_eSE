#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# date        :2018/1/
# discriptions :
# vision      :
# copyright   :All copyright reserved by FMSH company
__author__ = 'zuodengbo'
import os
import sys
from logging.handlers import RotatingFileHandler
import logging

LOG_PATH_FILE = os.path.split(os.path.realpath(__file__))[0] + "\\" + "apdu_interaction.log"
LOG_MODE = 'a'
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10M
LOG_MAX_FILES = 5  # 4 Files: Cap2Cos.log.1, Cap2Cos.log.2, Cap2Cos.log.3, Cap2Cos.log.4
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s %(levelname)-10s[%(filename)s:%(lineno)d(%(funcName)s)] %(message)s"
handler = RotatingFileHandler(LOG_PATH_FILE, LOG_MODE, LOG_MAX_SIZE, LOG_MAX_FILES)
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)