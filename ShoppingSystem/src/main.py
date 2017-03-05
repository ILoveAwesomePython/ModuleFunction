#主逻辑交互程序
import re
from src import logger
from src import auth
from src import accounts
from src import transaction
from config import settings

#trasaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')

#temp account data, only saves the data in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

@auth.login_required
def account_info(user_data):
    account_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = '''
       --------- ACCOUNT INFO --------
                 Account:     %s
                 Credit :     %s
                 Balance:     %s
                 Expire Date: %s''' \
                      % (account_data['id'], account_data['credit'], account_data['balance'],account_data['expire_date'])
    print(current_balance)
    s = input("b is back,q is exit:")
    if s == 'b':
        return
    elif s == 'q':
        logout(user_data)

@auth.login_required
def repay(user_data):
    account_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
                 Credit :    %s
                 Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    is_exit = False
    while not is_exit:
        repay_amount = input('Input repay amount:(input q to back)').strip()
        if repay_amount == 'q':
            is_exit = True
        elif len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay',repay_amount)
            if new_balance:
                print('New Balance:%s'%new_balance)
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)


@auth.login_required
def withdraw(user_data):
    account_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
                     Credit :    %s
                     Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    is_exit = False
    while not is_exit:
        withdraw_amount = input('Input withdraw amount:(input q to back)').strip()
        if withdraw_amount == 'q':
            is_exit = True
        elif len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('New Balance:%s' % new_balance)
        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

@auth.login_required
def transfer(user_data):
    account1_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
                         Credit :    %s
                         Balance:    %s''' % (account1_data['credit'], account1_data['balance'])
    print(current_balance)
    is_exit = False
    while not is_exit:
        trans_user = input("Please enter account id for transfer:(input q to back)")
        if trans_user == 'q':
            is_exit = True
        else:
            account2_data = accounts.load_current_balance(trans_user)
            if account2_data:
                transfer_amount = input('Input transfer amount:').strip()
                if len(transfer_amount) > 0 and transfer_amount.isdigit():
                    new_balance_account1 = transaction.make_transaction(trans_logger, account1_data, 'transfer_account1', transfer_amount)
                    transaction.make_transaction(trans_logger, account2_data, 'transfer_account2', transfer_amount)
                    if new_balance_account1:
                        print('New Balance:%s' % new_balance_account1)
                else:
                    print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)


@auth.login_required
def pay_check(user_data):
    account_log = "account:%s"%user_data['account_id']
    log_file = "%s/log/%s" % (settings.BASE_DIR, "transactions.log")
    with open(log_file,'r') as f:
        for i in f:
            if account_log in i:
                print(i)
    s = input("b is back,q is exit:")
    if s == 'b':
        return
    elif s == 'q':
        logout(user_data)

@auth.login_required
def logout(user_data):
    account_data = accounts.load_current_balance(user_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
                             Credit :    %s
                             Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None
    }
    exit("ByeBye")

@auth.login_required
@auth.admin_required
def add_account(user_data):
    is_exit = False
    while not is_exit:
        account_detail = input("Please enter CardID|Password|ExpireDate:")
        if re.match(r'(\d+)\|(.+)\|(\d{4}-\d{2}-\d{2})',account_detail):
           account_details = account_detail.split('|')
           print(account_details)
           accounts.add_account(*account_details)

@auth.login_required
@auth.admin_required
def check_account(user_data):
    user_id = input("Please enter user card ID:")
    account_data = accounts.load_current_balance(user_id)
    if account_data['status'] == 1:
        freeze_status = 'Y'
    else:
        freeze_status = 'N'
    current_balance = '''
          --------- ACCOUNT INFO --------
                    Account:     %s
                    Credit :     %s
                    Balance:     %s
                    Expire Date: %s
                    Enroll Date: %s
                    Pay Day:     %s
                    Freeze:      %s ''' % (
                      account_data['id'], account_data['credit'], account_data['balance'],
                      account_data['expire_date'],account_data['enroll_date'],account_data['pay_day'],
                      freeze_status
                      )
    print(current_balance)
    s = input("b is back,q is exit:")
    if s == 'b':
        return
    elif s == 'q':
        logout(user_data)

@auth.login_required
@auth.admin_required
def freeze_account(user_data):
    user_id = input("Please enter user card ID:")
    account_data = accounts.load_current_balance(user_id)
    if account_data:
        accounts.set_freeze(account_data)


def interactive(user_data):
    menu = u'''

             ------- Bank ---------
             \033[32;1m
             1.  账户信息
             2.  还款
             3.  取款
             4.  转账
             5.  账单
             6.  退出
             \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout
    }
    is_exit = False
    while not is_exit:
        print(menu)
        user_select = input("Please select operation:")
        if user_select in menu_dic:
            menu_dic[user_select](user_data)


def admin_manage(user_data):
    info = '''
    ----------------- Manage Menus------------
    1. 添加用户
    2. 查看用户信息
    3. 冻结用户
    '''
    info_dic = {
        '1': add_account,
        '2': check_account,
        '3': freeze_account
    }
    is_exit = False
    while not is_exit:
        input(info)
        admin_operation = input("Please select operation")
        if admin_operation in info_dic:
            info_dic[admin_operation](user_data)
        else:
            print("The operation doesn't exist")


def user_run():
    '''

    :return:
    '''

    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
    else:
        print("Please login first")


def admin_run():
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        if acc_data.get('is_managed') == 1:
            admin_manage(user_data)
        else:
            print("You don't have permission")
    else:
        print("Please login first")


