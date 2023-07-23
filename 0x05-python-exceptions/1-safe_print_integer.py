#!/usr/bin/python3
def safe_print_integer(value):
	try:
		print("{:d}".format(value))
	except (ValueError, TypeError):
		print("it is not an integer")
		return False
	return True
