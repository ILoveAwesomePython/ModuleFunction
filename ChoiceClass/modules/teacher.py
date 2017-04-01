#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

class teacher(object):
    def __init__(self,teacher_name,teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.class_teach = {}

    def add_class(self,class_name,class_obj):
        self.class_teach[class_name] = class_obj
