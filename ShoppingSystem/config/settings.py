import os
import logging
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = str(datetime.date.today())

DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

DATABASE_ADMIN = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'admins',
    'path': "%s/db" % BASE_DIR
}

DATABASE_MODLE = {
    "id": None,
    "password": None,
    "expire_date": None,
    "balance": 15000,
    "enroll_date":today,
    "credit": 15000,
    "pay_day": 22,
    "status": 0,
    "is_managed": 0
}

TRANSACTION_TYPE = {
    'repay': {'action':'plus','interest':0},
    'withdraw': {'action':'minus','interest':0.05},
    'transfer_account1': {'action':'minus','interest':0.05},
    'transfer_account2': {'action':'plus','interest':0},
    'consume': {'action':'minus','interest':0},
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}
