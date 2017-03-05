#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import re
from src import priority

def run():
    cal = input("calculator:")
    if re.match("[0-9,.,*,/,+,-]+",cal):
        result = priority.calculate(cal)
        print(result)