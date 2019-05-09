#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   search.py
@Time    :   2019/05/09 12:57:17
@Author  :   Txh
@Version :   1.0
@Contact :   849366508@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

"""
课   时间
1-2  8:00-10:00
3-4  10:00-12:00
5-6  13:00-15:00
7-8  15:00-17:00
9=10 18:00-20:00
"""
import parse as ps
import pandas as pd
import datetime

firstday = 
rooms = ps.parseSeat()

def check(roomid,date,time,seat):
    #教室id、日期、时间、座位，时间包含小时hour分钟min两个int,return空闲时间
    #日期格式
    rooms[roomid]
    