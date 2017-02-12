import re
def equal(db_data, where_data):
    return db_data == where_data

def greater_than(db_data, where_data):
    return db_data > where_data

def less_than(db_data, where_data):
    return db_data < where_data

def like(db_data, where_data):
    where_data = where_data.strip("'")
    where_data = where_data.replace(r'%', r'.*')
    pattern = where_data.replace(r'_', r'.')
    return re.match(pattern, db_data) is not None