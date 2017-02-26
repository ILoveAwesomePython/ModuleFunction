#主逻辑交互程序
from src import logger
from src import auth
from src import accounts
from src import transaction

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


def pay_check():
    pass

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

def interactive(user_data):
    menu = u'''

             ------- Bank ---------
             \033[32;1m
             1.  账户信息
             2.  还款(功能已实现)
             3.  取款(功能已实现)
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
        user_select = input("Please select opertation:")
        if user_select in menu_dic:
            menu_dic[user_select](user_data)



def run():
    '''

    :return:
    '''

    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)