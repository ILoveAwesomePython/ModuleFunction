#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) )

STAFF_DB = os.path.join(BASE_DIR, 'db', 'StaffInf.json')

INSERT_INVALID_INPUT ='''
Check insert-values should have 4;
SQL format should be like: INSERT INTO Persons values ('139','sb','IT','21')
'''


SELECT_INVALID_INPUT ='''
Check insert-values should have 4;
SQL format should be like:  SELECT * FROM Persons
                          or SELECT id, LastName,FirstName FROM Persons
                          or SELECT age,name FROM Persons where age = 22, name like '%amapi'
                          (where syntax should has space)
'''

UPDATE_INVALID_INPUT ='''
Check insert-values should have 4;
SQL format should be like:  update persons set name = 'hello',age = 22 where staff_id = 1
                          or update persons set phone = '139',age = 22
                          or update persons set phone = '139',name = '233' where age = 22, name like '%amapi'
                          (where syntax should has space)
'''


DB_COLUMN = json.load(open(STAFF_DB, "r"))[0].keys()

SYMBOL = {
	'=':'equal',
	'>':'greater_than',
	'<':'less_than',
	'like':'like'
}