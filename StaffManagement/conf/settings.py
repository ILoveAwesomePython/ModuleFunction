#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) )

STAFF_DB = os.path.join(BASE_DIR, 'db', 'StaffInf.json')

INSERT_INVALID_INPUT ='''
Check insert-values should have 4;
SQL format should be like: INSERT INTO Persons values ('139','sb','IT','21')
'''


INSERT_INVALID_INPUT ='''
Check insert-values should have 4;
SQL format should be like:  SELECT * FROM Persons
                          or SELECT LastName,FirstName FROM Persons
                          or SELECT LastName,FirstName FROM Persons where id>1111
'''