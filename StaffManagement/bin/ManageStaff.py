#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import os
import sys
# Add root folder to sys.path in order import convinience
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) ))

from modules import auth,\
                    view
import re
def run():
    # if auth.login():
    print('Welcom')

    sql = input("Input SQL: ").lower().strip()
    # Extract SQL action
    action = re.match(r'(\w*)\b', sql)
    if action:
        action = action.group(0)
    else:
        print('Invalid SQL')

    # execute function according to SQL
    func = getattr(view, action, None)
    if func:
        func(sql)
    else:
        print('Invalid SQL')

# else:
#     print('Login first!')


if __name__ == '__main__':
    run()