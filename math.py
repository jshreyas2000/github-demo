def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	if y==0:
		return DIVIDE_BY_ZERO_ERROR
	else:
		return x/y