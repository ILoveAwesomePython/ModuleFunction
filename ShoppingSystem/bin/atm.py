# ATM 执行程序即启动程序,启动程序里面不写逻辑

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) ))

from src import main

if __name__ == '__main__':
    account_type_des = '''
    1. user
    2. admin
    '''
    print(account_type_des)
    account_type = input("Please select user type:")
    if account_type == '1':
        main.user_run()
    elif account_type == '2':
        main.admin_run()
    else:
        print("The account type doesn't exist")

