#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu


def registers():
    school = input("Please select a school:")


def charge():
    pass

def choice_class():
    pass

def exit():
    pass


def student_role():

    oper= '''
    --------choice------
    1. register
    2. charge
    3. choice class
    4. exit
    '''
    oper_dict = {
        '1' : 'register',
        '2' : 'charge',
        '3' : 'choice_class',
        '4' : 'exit'
    }
    is_back = False
    while not is_back:
        print(oper)
        s = input("Please select operation:")
        if s in oper_dict:
            oper_dict[s]()


