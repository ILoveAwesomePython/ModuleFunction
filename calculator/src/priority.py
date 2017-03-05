#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import re


def calculate(cal):
    cal_result = one_prio(cal)
    return cal_result


def one_prio(cal):
    is_one_prio = True
    while is_one_prio:
        gr = re.search("[(]([0-9,.,*,/,+,-]+)[)]", cal)
        if gr:
            prio2_result = two_prio(gr.group(1))
            prio3_result = three_prio(prio2_result)
            cal = re.sub("[(]([0-9,.,*,/,+,-]+)[)]",prio3_result, cal, 1)
        else:
            prio2_result = two_prio(cal)
            prio3_result = three_prio(prio2_result)
            cal = prio3_result
            is_one_prio = False
    return cal


def two_prio(cal_01):
    is_two_prio = True
    while is_two_prio:
        gr_02 = re.search(r"(\d+)([*,/])(\d+)",cal_01)
        if gr_02:
            if gr_02.group(2) == '*':
                result = float(gr_02.group(1)) * float(gr_02.group(3))
            else:
                result = float(gr_02.group(1)) / float(gr_02.group(3))
            result_s = "%d" % result
            cal_01 = re.sub(r"\d+[*,/]\d+", result_s, cal_01, 1)
        else:
            is_two_prio = False
    return cal_01


def three_prio(cal_02):
    is_three_prio = True

    while is_three_prio:
        gr_03 = re.search(r"(\d+)([+,-])(\d+)", cal_02)
        if gr_03:
            if gr_03.group(2) == '+':
                result = float(gr_03.group(1)) + float(gr_03.group(3))
            else:
                result = float(gr_03.group(1)) - float(gr_03.group(3))
            result_s = "%d" % result
            cal_02 = re.sub(r"\d+[+,-]\d+", result_s, cal_02, 1)
        else:
            is_three_prio = False
    return cal_02