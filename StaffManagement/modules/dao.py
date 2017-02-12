#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import json
from conf import settings


def create(user_input):
    try:
        json.dump(user_input,open(settings.STAFF_DB,"w"))
        print("Create successful!")
    except Exception as e:
        print(e.value)


def delete():
    pass


def update():
    pass


def select():
    pass

def db_datas():
	return json.load(open(settings.STAFF_DB, "r"))
