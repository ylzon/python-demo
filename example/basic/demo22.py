#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python日志模块
"""

import logging

logging.basicConfig(
    filename="base.log",
    format="[%(lineno)d]%(asctime)s - %(pathname)s - %(levelname)-8s - %(module)s : %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10, 'log')
