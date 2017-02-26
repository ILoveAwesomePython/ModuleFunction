#数据库连接引擎
from config import settings
import os
import json

def file_db_handle(conn_params):
    print('file db:',conn_params)
    return  file_execute


def db_handler():
    conn_params = settings.DATABASE
    if conn_params['engine']=='file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass

def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'],conn_params['name'])

    sql_list = sql.split('where')
    if sql_list[0].startswith("select") and len(sql_list)>1:
        column,val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = '%s/%s.json'%(db_path,val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file,'r') as f:
                   account_data = json.load(f)
                   return account_data
            else:
                print("The user information doesn't exist")
        else:
            print("The account is necessary")

    if sql_list[0].startswith("update") and len(sql_list)>1:
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = '%s/%s.json'%(db_path,val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file, 'w') as f:
                    json.dump(kwargs['account_data'],f)
            else:
                print("The user information doesn't exist")
        else:
            print("The account is necessary")

    else:
        print("invalid sql")


