#用于从文件里加载和存储账户数据
from src import db_handler

def load_current_balance(account_id):
    db_api = db_handler.db_handler()
    account_data = db_api("select * from accounts where account=%s" % account_id)
    return account_data

def dump_account(account_data):
    db_api = db_handler.db_handler()
    db_api("update set account where account=%s" %account_data['id'],account_data=account_data)
