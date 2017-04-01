#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu

class student(object):
    def __init__(self,student_name,student_age):
        self.student_name = student_name
        self.age = student_age
        self.feed = 0

    def add_feed(self,feed):
        self.feed += feed

    def reduce(self,feed):
        self.feed -= feed