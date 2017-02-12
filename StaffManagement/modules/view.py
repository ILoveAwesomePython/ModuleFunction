#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import re
from datetime import date
from conf import  settings
from .lib import *
from .dao import *


def insert(sql):
    # Extract create data
    regex =r"values \('(?P<phone>\w+)','(?P<name>\w+)','(?P<dept>\w+)','(?P<age>\w+)'\)"
    matched = re.search(regex, sql)

    if matched:
        insert_data = matched.groupdict()
        if insert_data['age'].isdigit():
            if validate_phone(insert_data['phone']):
                insert_data['enroll_date'] = str(date.today())
                insert_data['staff_id'] = staff_id()

                datas = db_datas()
                datas.append(insert_data)

                create(datas)

            else:
                print('Phone is not valid')
        else:
            print('Age is illegal')
    else:
        print(settings.INSERT_INVALID_INPUT)

def select(sql):
    print(sql)

def update(sql):
    pass

def delete(sql):
    pass