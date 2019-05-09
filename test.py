#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/05/09 10:49:03
@Author  :   Txh
@Version :   1.0
@Contact :   849366508@qq.com
@License :   (C)Copyright 2019-2020
@Desc    :   None
'''

# here put the import lib

import datetime


def test():
    yes = datetime.datetime(2019, 5, 8)
    print((datetime.datetime.now()-yes).days)
    print(yes.hour)


test()
