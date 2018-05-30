#1

def if_number(number):

	if type(number) == int:
		print("True")
	else: 
		print("False")

if_number(10)


#2

def if_even(number):

	if number % 2 == 0:
		print("Number is even")

	else:
		print("Number is not even")
if_even(2)

#3

def if_odd(number):
	if number % 2 != 0:
		print("Number is odd")

	else:
		print("NUmber is not odd")

if_odd(3)



#4

def if_name(name):

	if name == "Anton":
		print("My name is {}".format(name))

	else:
		print("The name is not Anton")


if_name("Anton")



#5

def if_string(sample):

	if type(sample) == str:
		print("Input is a string")

	else:
		print("Input is not a string")


if_string("Hello")


#6

def if_equal(value1,value2):

	if value1 == value2:
		print("Value 1: {} and Value 2: {} are equal".format(value1,value2))


	else:
		print("Value 1: {} and Value 2: {} are not equal".format(value1,value2))


if_equal(1,2)



#7

def if_list(list1):

	if type(list1) == list:
		print("This is a list")

	else:
		print("This is not a list")

sample = []
if_list(sample)


#8

def if_multiple_of_five(number):

	if number % 5 == 0:
		print("The number {} is a multiple of 5".format(number))

	else:
		print("The number {} is not a multiple of 5".format(number))


if_multiple_of_five(25)



#9

def if_bigger(num1, num2):

	if num1 > num2:
		print("The first number is bigger than the second number")

	elif num2 > num1:
		print("The second number is bigger than the first number")


if_bigger(3,5)


#10
def if_smaller(num1, num2):

	if num1 < num2:
		print("The first number is smaller than the second number")

	elif num2 < num1:
		print("The second number is smaller than the first number")


if_smaller(3,5)