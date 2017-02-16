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
    if 'where' in sql:
        where_regex = r'select (.*) from persons where (.*)'
        matched = re.search(where_regex, sql)
        if matched:
            column, where_datas = matched.groups(0)

            column_to_validate = column.split(',')
            column_to_validate += make_columns(where_datas)

            if validate_column(column_to_validate):
                filtered_datas = where_filter(where_datas)
                if filtered_datas:
                    show_data(filtered_datas, column)
                else:
                    print('Nothing matched')
            else:
                print('Your select field is not valid, check no blank between fields')

        else:
            print(settings.SELECT_INVALID_INPUT)

    else:
        regex = r'select (.*) from'
        matched = re.search(regex, sql)
        if matched:
            column = matched.groups(0)[0]
            if validate_column(column.split(',')):
                show_data(db_datas(), column)
            else:
                print('Your select field is not valid, check no blank between fields')

        else:
            print(settings.SELECT_INVALID_INPUT)



def update(sql):
    # TODO: need change the name, != dao update
    regex = ''
    column_to_validate = ''
    where_datas = ''

    if 'where' in sql:
        regex = r'update persons set (.*) where (.*)'
        matched = re.search(regex, sql)
        if matched:
            set_datas, where_datas = matched.groups()
            column_to_validate = make_columns("%s,%s" % (set_datas, where_datas))
        else:
            print(settings.SELECT_INVALID_INPUT)
    else:
        regex = r'update persons set (.*)'
        matched = re.search(regex, sql)
        if matched:
            set_datas = matched.groups()[0]
            column_to_validate = make_columns(set_datas)
        else:
            print(settings.SELECT_INVALID_INPUT)

    
    if validate_column(column_to_validate):
        if 'phone' in set_datas:
            phone = re.search(r"phone = '([0-9]*)'", set_datas).groups(0)[0]
            if validate_phone(phone):
                db_update(set_datas, where_datas)
            else:
                print('Phone is not valid')
        else:
            db_update(set_datas, where_datas)
    else:
        print('Your select field is not valid, check no blank between fields')
        

def delete(sql):
    pass