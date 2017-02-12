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
    if 'where' in sql:
        where_regex = r'select (.*) from persons where (.*)'
        matched = re.search(where_regex, sql)
        if matched:
            column, where_datas = matched.groups(0)

            column_to_validate = column.split(',')
            column_to_validate += where_data_column(where_datas)

            if validate_column(column_to_validate):
                if where_filter(where_datas):
                    # print(where_filter(where_datas))
                    show_data(where_filter(where_datas), column)
                else:
                    print('Nothing matched')
            else:
                print('Your select filed is not valid')

        else:
            print(settings.SELECT_INVALID_INPUT)

    else:
        regex = r'select (.*) from'
        matched = re.search(regex, sql)
        if matched:
            column = matched.groups(0)
        else:
            print(settings.SELECT_INVALID_INPUT)



def update(sql):
    pass

def delete(sql):
    pass