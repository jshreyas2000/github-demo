# Add implementation
def add(x,y):
	return x+y

# Subtract implementation
def subtract(x,y):
	return x-y           #On master branch

# Multiply implementation
def multiply(x,y):
	return x*y           #On Bug456 branch

# Divide implementation
def divide(x,y):
	if y==0:             #On Master branch
		return DIVIDE_BY_ZERO_ERROR
	else:
		return x/y

def square(x):
	pass