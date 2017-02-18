#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import json
import hashlib
from operator import itemgetter

from conf import settings
from .dao import *
from modules import where_function


def validate_phone(phone):
    if not phone.isdigit():
        return False
    for db_staff in db_datas():
        if db_staff['phone'] == phone:
            return False
    return True

def validate_column(column):
    column = set(column)
    db_column = set(settings.DB_COLUMN)
    if '*' in column:
        column.remove('*')
    return column.issubset(db_column)

def make_columns(datas):
    '''
    REeturn list of where column
    '''  
    datas = datas.split(',')
    columns = list(map(lambda data: data.strip().split(' ')[0],
                datas))
    return columns

def staff_id():
    db_staffs = db_datas()
    sorted_staffs= sorted(db_staffs, 
        key = itemgetter('staff_id'))

    max_staff_id = sorted_staffs[len(sorted_staffs)-1]['staff_id']
    return str(max_staff_id + 1)


def where_filter(where_datas):
    filtered_data = []

    where_datas = where_datas.split(',')
    for db_data in db_datas():
        is_satisfy = []
        for where_data in where_datas:
            column, operation, condition= where_data.strip().split(' ')
            #print('column %s, op %s, con %s' %(column, operation, condition))
            func = settings.SYMBOL.get(operation, None)
            if not func:
                return None

            func = getattr(where_function, func, None)
            is_satisfy.append( func(str(db_data[column]), condition) )

        if all(is_satisfy):
            filtered_data.append(db_data)

    return filtered_data


def where_satisfied(where_datas, data):
    where_datas = where_datas.split(',')
    is_satisfy = []

    for where_data in where_datas:
        column, operation, condition= where_data.strip().split(' ')
        func = settings.SYMBOL.get(operation, None)
        if not func:
            return None

        func = getattr(where_function, func, None)
        is_satisfy.append( func(str(data[column]), condition) )

    if all(is_satisfy):
        return True
    else:
        return False


def show_data(datas, column):
    up = ' Search Info Count: %s ' % len(datas)
    print(up.center(55, '*'))
    if column == '*':
        column = datas[0].keys()
    else:
        column = column.split(',')

    for data in datas:
        print(('staff %s' % data['staff_id']).center(55,'='))
        for item in column:
            if item != 'password':# Do not show password!
                print('{column}:{value}'.format(column=item, value=data[item]) )

def hashed(base_password):
    m = hashlib.md5(b'hello world')
    m.update(bytes(base_password, encoding='utf-8'))
    return m.hexdigest()


