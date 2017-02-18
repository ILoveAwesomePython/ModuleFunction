from modules import lib, dao


def login(func):
	def decorator(*args, **kwargs):
		db_datas = dao.db_datas()

		staff_id = input('sid: ').strip()
		password = lib.hashed(input('password: '))

		for data in db_datas:
			if (data['staff_id'] == staff_id and \
				data['password'] == password):
				result = func(*args, **kwargs)
				return func

		print('Invalid credentials')

	return decorator