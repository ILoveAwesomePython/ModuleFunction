#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import json
from operator import itemgetter

from conf import settings
from .dao import *


def validate_phone(phone):
    if not phone.isdigit():
        return False
    for db_staff in db_datas():
        if db_staff['phone'] == phone:
            return False
    return True

def staff_id():
    db_staffs = db_datas()
    sorted_staffs= sorted(db_staffs, 
        key = itemgetter('staff_id'))
    
    max_staff_id = sorted_staffs[len(sorted_staffs)-1]['staff_id']
    return max_staff_id + 1