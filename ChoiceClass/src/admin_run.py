#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import re
import pickle
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.school import school
from config import setting

def add_school():
    schools = []
    is_exit = False
    while not is_exit:
        school_info = input("Please enter SchoolName|SchoolAddress(b is back):")
        if re.search(r"\|",school_info):
            school_info = school_info.split('|')
            with open(setting.SCHOOL_FILE,'rb') as fp:
                # data = fp.read()
                # school_file = pickle.loads(data)
                school_file = pickle.load(fp)
            for i in school_file:
                if i.school_name == school_info[0] and i.school_addr == school_info[1]:
                    print("This school is existent")
                    break
                schools.append(i)
            else:
                school_obj = school(school_info[0], school_info[1])
                schools.append(school_obj)
                with open(setting.SCHOOL_FILE, 'wb') as fp:
                    pickle.dump(schools,fp)
                print("The school %s created"%school_info[0])
        elif school_info == 'b':
            is_exit = True
        else:
            print("Please enter valid school information like 上海|青泥洼桥")

def add_lesson():
    n = 1
    is_exit = False
    while not is_exit:
        with open(setting.SCHOOL_FILE,'rb') as fp:
            schools = pickle.load(fp)
        print("Schools".center(20,'-'))
        for school in schools:
            print("%s. %s %s"%(n,school.school_name,school.school_addr))
            n += 1
        s = input("Please select a school(b is back):")
        s = int(s) if s.isdigit() else s
        if s < n:
            lesson_info = input("Please enter lesson name|lesson time|lesson price:")
            if re.findall(r"\|", lesson_info):
                lesson_info = lesson_info.split('|')
                schools[s-1].lesson_creation(lesson_info[0],lesson_info[1],lesson_info[2])
                with open(setting.SCHOOL_FILE, 'wb') as fp:
                    pickle.dump(schools, fp)
                print("The %s lesson created"%lesson_info[0])
            else:
                print("Please enter valid lesson information like Python|2017-01-01|6000")
        elif s == "b":
            is_exit = True
        else:
            print("Please select existent school!")

def add_teacher():
    n = 1
    is_exit = False
    while not is_exit:
        with open(setting.SCHOOL_FILE,'rb') as fp:
            schools = pickle.load(fp)
        print("Schools".center(20,'-'))
        for school in schools:
            print("%s. %s %s"%(n,school.school_name,school.school_addr))
            n += 1
        s = input("Please select a school(b is back):")
        s = int(s) if s.isdigit() else s
        if s < n:
            teacher_info = input("Please enter teacher name|teacher salary:")
            if re.findall(r"\|", teacher_info):
                teacher_info = teacher_info.split('|')
                schools[s-1].teacher_creation(teacher_info[0],teacher_info[1])
                with open(setting.SCHOOL_FILE, 'wb') as fp:
                    pickle.dump(schools, fp)
                print("The %s lesson created"%teacher_info[0])
            else:
                print("Please enter valid teacher information like Mao|10000")
        elif s == "b":
            is_exit = True
        else:
            print("Please select existent school!")


def add_class():
    n = 1
    m = 1
    is_exit = False
    while not is_exit:
        with open(setting.SCHOOL_FILE,'rb') as fp:
            schools = pickle.load(fp)
        print("Schools".center(20,'-'))
        for school in schools:
            print("%s. %s %s"%(n,school.school_name,school.school_addr))
            n += 1
        s = input("Please select a school(b is back):")
        s = int(s) if s.isdigit() else s
        if s<n:
            lesson_info = input("Please enter class name:")
            print("Teachers".center(20, '-'))
            for teacher in schools[s-1].teachers:
                print("%s. %s"%(s,teacher))
            t = input("Please select a teacher:")
            t = int(t) if t.isdigit() else t



        elif s=="b":
            is_exit = True
        else:
            print("Please select existent school!")


def exit():
    pass


# def check_school(school_info):
#     with open(setting.SCHOOL_FILE, 'rb') as fp:
#         # data = fp.read()
#         # school_file = pickle.loads(data)
#         school_file = pickle.load(open(setting.SCHOOL_FILE, 'rb'))
#     for i in school_file:
#         if i.school_name == school_info[0] and i.school_addr == school_info[1]:
#             return i
#     else:
#         return False




def admin_role():

    oper= '''
    --------choice------
    1. add school
    2. add lesson
    3. add teacher
    4. add class
    5. exit
    '''
    oper_dict = {
        '1' : add_school,
        '2' : add_lesson,
        '3' : add_teacher,
        '4' : add_class,
        '5' : exit
    }
    is_back = False
    while not is_back:
        print(oper)
        s = input("Please select operation:")
        if s in oper_dict:
            oper_dict[s]()
