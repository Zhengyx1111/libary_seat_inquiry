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

firstday = datetime.datetime(2019, 3, 4)
timetable = {1: 8, 2: 10, 3: 10, 4: 12, 5: 13, 6: 15, 7: 15, 8: 17, 9: 18, 10: 20}
rooms = ps.parseSeat()


def check(roomid, date):
    # 教室id、日期时间,return空闲时间
    # 日期格式datetime
    week = (date-firstday)//7+1
    for seat in rooms[roomid].seatlist:
        lessons = seat.student.class_.lesson
        for lesson in lessons:
            if(week in lesson.week):
<<<<<<< HEAD
                if(lesson.single_or_double == 'single' and week % 2 == 0):
                    return -1
                elif(lesson.single_or_double == 'double' and week % 2 == 1):
                    return -1
                elif(date.hour >= timetable[lesson.start_hour] and date.hour < timetable[lesson.end_hour]):
=======
                if(date.hour >= timetable[lesson.start_hour] and date.hour <= timetable[lesson.end_hour]):
>>>>>>> bf9f3b6afadcd0bef94f980c993ae47f9dcd8ff1
                    return (timetable[lesson.end_hour]-date.hour)*60+60-date.minute
                else:
                    return 0
            else:
                return -1


if __name__ == '__main__':
    date = datetime.datetime.now()
    check(1, date)
