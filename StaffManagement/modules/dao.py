#!/user/bin/env python
# -*-coding:utf-8 -*-
# Author: Amy Wu
import json
from conf import settings
from modules import lib

def create(user_input):
	try:
		json.dump(user_input, open(settings.STAFF_DB,"w"))
		print("Create successful!")
	except Exception as e:
		print(e.value)

def set_values(set_datas, data):
	for item in set_datas:
		column, operation, value = item.split(' ')
		value = value.strip("'") # there is quote

		if column == 'phone':
			if lib.validate_phone(value):
				data[column] = value
		elif column == 'password':
			data[column] = lib.hashed(value)
		else:
			data[column] = value

def db_update(set_datas, where_datas):
	print(set_datas)
	print(where_datas)
	set_datas = set_datas.split(',')

	datas = db_datas()
	if where_datas:
		for data in datas:
			if lib.where_satisfied(where_datas, data):
				set_values(set_datas, data)
				# Change db in real time: once update one write into db
				json.dump(datas, open(settings.STAFF_DB,"w"))
	else:
		for data in datas:
			set_values(set_datas, data)
			# Change db in real time: once update one write into db
			json.dump(datas, open(settings.STAFF_DB,"w"))


def select():
	pass

def db_datas():
	return json.load(open(settings.STAFF_DB, "r"))
