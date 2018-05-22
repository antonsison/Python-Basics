#Basic Arithmetic Operators

#Addition
num = 10 + 10
print (num) #20

#Subtraction
num = 20 -15
print (num) #5

#Multiplication
num = 5 * 5
print (num) #25

#Divvision
num = 100 / 20
print (num) #5

#Modulus
num = 10 % 3
print (num) #1

#Exponent
num = 3 ** 2
print (num) #9

#Floor Division (round up if negative)
#no decimal
num = -11//3
print (num) #-4

#Boolean Operators

# or

# and

# not


#Comparison Operators

# ==
def sample(a,b):
	if a == b:
		print(True)  
	else:      
		print(False)

sample(1,2) #False

# >

def sample(a,b):
	if a > b:
		print(True)  
	else:      
		print(False)

sample(3,2) #True

# <
def sample(a,b):
	if a < b:
		print(True)  
	else:      
		print(False)

sample(3,2) #False

# != or <>
def sample(a,b):
	if a != b:
		print(True)  
	else:      
		print(False)

sample(5,1) #True

# >=
def sample(a,b):
	if a >= b:
		print(True)  
	else:      
		print(False)

sample(7,7) #True

# <=
def sample(a,b):
	if a <= b:
		print(True)  
	else:      
		print(False)

sample(9,7) #False


#Assignment Operators
# = 
def sample(a,b):
	c = a + b
	print(c)

sample(2,3) #5

# +=
def sample(c,a):
	c += a
	print(c)

sample(1,2) #3

# +=
def sample(c,a):
	c -= a
	print(c)

sample(1,2) #-1

# *=
def sample(c,a):
	c *= a
	print(c)

sample(1,2) #2

# /=
def sample(c,a):
	c /= a
	print(c)

sample(1,2) #0.5

# %=
def sample(c,a):
	c %= a
	print(c)

sample(1,2) #1

# **=
def sample(c,a):
	c **= a
	print(c)

sample(2,2) #4

# //=
def sample(c,a):
	c //= a
	print(c)

sample(-11,3) #-4