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
        gr = re.search("\([^()]*\)",cal)
        if gr:
            prio1_result = gr.group().strip('()')
            prio2_result = two_prio(prio1_result)
            prio3_result = three_prio(prio2_result)
            cal = re.sub("\([^()]*\)",prio3_result, cal, 1)
            cal = cal.replace(" ","")
        else:
            prio2_result = two_prio(cal)
            prio3_result = three_prio(prio2_result)
            cal = prio3_result
            cal.replace(" ","")
            is_one_prio = False
    return cal


def two_prio(cal_01):
    is_two_prio = True
    while is_two_prio:
        gr_02 = re.search(r"(\-?\d+\.?\d*)([*,/])(\-?\d+\.?\d*)", cal_01)
        if gr_02:
            if gr_02.group(2) == '*':
                result = float(gr_02.group(1)) * float(gr_02.group(3))
            else:
                result = float(gr_02.group(1)) / float(gr_02.group(3))
            result_s = "%f" % result
            cal_01 = re.sub(r"\-?\d+\.?\d*[*,/]\-?\d+\.?\d*", result_s, cal_01, 1)
        else:
            is_two_prio = False
        cal_01 = cal_01.replace(" ","")
    return cal_01


def three_prio(cal_02):
    is_three_prio = True

    while is_three_prio:
        gr_03 = re.search(r"(\-?\d+\.?\d*)([+,\-])(\-?\d+\.?\d*)", cal_02)
        if gr_03:
            if gr_03.group(2) == '+':
                result = float(gr_03.group(1)) + float(gr_03.group(3))
            else:
                result = float(gr_03.group(1)) - float(gr_03.group(3))
            result_s = "%f" % result
            cal_02 = re.sub(r"\-?\d+\.?\d*[+,-]\-?\d+\.?\d*", result_s, cal_02, 1)
        else:
            is_three_prio = False
        cal_02 = cal_02.replace(" ","")
    return cal_02