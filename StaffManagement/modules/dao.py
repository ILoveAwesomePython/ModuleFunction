#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import json
from conf import settings

def create(*args):
    try:
        json.dump(args,open(settings.STAFF_DB,"w"))
        print("Create successful!")
    except Exception as e:
        print(e.value)


def delete():
    pass


def update():
    pass


def select():
    pass