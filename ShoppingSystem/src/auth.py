from src import db_handler
import time

def acc_auth(account,password):
    db_api = db_handler.db_handler()#数据访问接口一致
    data = db_api("select * from accounts where account=%s" % account)
    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("Your card has expired")
        else:
            return data
    else:
        print("Invalid account or password")


def acc_login(user_data,log_obj):

    retry_count = 0
    while not user_data['is_authenticated'] and retry_count < 3:
        account = input("account:").strip()
        password = input("password:").strip()
        auth = acc_auth(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        else:
            retry_count += 1
    else:
        log_obj.error( "account [%s] too many login attempts" % account )
        exit()


def login_required(func):
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated') == True:
            return func(args[0])
        else:
            exit("User is not authenticated")
    return wrapper


