#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pickle
from modules import lesson
from modules import school_class
from modules import teacher
from modules import student
from config import setting

class school(object):
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.lessons = {}
        self.classes = {}
        self.teachers = {}
        self.students = {}
        #pickle.dump(self,open(setting.LESSON_FILE ,'wb'))

    def lesson_creation(self,lesson_name,lesson_time,lesson_price):
        #school_info = pickle.load(open("school",'r'))
        lesson_01 = lesson.lesson(lesson_name,lesson_time,lesson_price)
        self.lessons[lesson_name] = lesson_01
        #pickle.dump(lessons,open(setting.LESSON_FILE ,'wb'))

    def class_creation(self,class_name,lesson_obj,teacher_obj):
        class_01 = school_class.school_class(class_name,lesson_obj,teacher_obj)
        self.classes[class_name] = class_01

    def teacher_creation(self,teacher_name,teacher_salary):
        teacher_01 = teacher.teacher(teacher_name,teacher_salary)
        self.teachers[teacher_name] = teacher_01

    def student_creation(self,student_name,student_age):
        student_01 = student.student(student_name,student_age)
        self.students[student_name] = student_01


# school01 = school("老男孩","上海")
# school02 = school("老男孩","北京")
# schools = []
# schools.append(school01)
# schools.append(school02)
# pickle.dump(schools, open(setting.SCHOOL_FILE, 'wb'))
# school01.lesson_creation("py","40 周","6000")

# school_file = pickle.load(open(setting.SCHOOL_FILE,'rb'))
# for i in school_file:
#     print(i.school_name)

