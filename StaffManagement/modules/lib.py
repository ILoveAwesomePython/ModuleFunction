#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import json
from conf import settings
from .dao import *

db_staffs = json.load(open(settings.STAFF_DB, "r"))
def validate_phone(phone):
    if not phone.isdigit():
        return False
    for db_staff in db_staffs:
        if db_staff['phone'] == phone:
            return False
    return True

def staff_id():
    last_id = db_staffs[len(db_staffs)-1]['staff_id']
    return  last_id + 1

def append_staff(**kwargs):
    db_staffs.append(kwargs)
    print(db_staffs)
    create(*db_staffs)