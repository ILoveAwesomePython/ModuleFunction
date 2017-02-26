import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',  # support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
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