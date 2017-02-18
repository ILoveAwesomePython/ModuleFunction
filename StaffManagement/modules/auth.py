from modules import lib, dao

USER = {'user':{}}


# def login(func):
# 	def decorator(*args, **kwargs):
# 		db_datas = dao.db_datas()

# 		staff_id = input('sid: ').strip()
# 		password = lib.hashed(input('password: '))

# 		for data in db_datas:
# 			if (data['staff_id'] == staff_id and \
# 				data['password'] == password):
# 				result = func(*args, **kwargs)
# 				return func

# 		print('Invalid credentials')

# 	return decorator

def sid_filter(db_data, staff_id):
	return db_data['staff_id'] == staff_id


def login(func):
	def decorator(*args, **kwargs):
		db_datas = dao.db_datas()

		staff_id = input('sid: ').strip()
		password = lib.hashed(input('password: '))

		user = list(filter(lambda db_data: sid_filter(db_data, staff_id), 
										db_datas))

		if user:
			USER['user'] = user[0]
			if user[0]['password'] == password:
				print('Login Success!')
				result = func(*args, **kwargs)
				return func
			else:
				print('Invalid credentials')
		else:
			print('Invalid credentials')

	return decorator

def is_admin(func):
	def decorator(*args, **kwargs):
		if USER['user']['admin'] == '1':
			result = func(*args, **kwargs)
			return result
		else:
			print('Permission denied')

	return decorator
