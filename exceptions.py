#1

def value_error():

	
	while True:
		try:
			number = int(input("Input a random number: "))

		except ValueError:
			print("Not a number! Please Try again!")

		else:
			print("This is the random number you gave us: {:d}".format(number))
			break

value_error()

#2
def import_error():

	try:
		import daOne
	except ImportError:
		print("Module does not exist")

	else:
		print("No errors!")

import_error()


#3

def keyboard_interrupt():

	while True:
		try:
			number = int(input("Input some number: "))

		except KeyboardInterrupt:
			print("Keyboard interrupted!")
			break

		else:
			print("No errors!")

keyboard_interrupt()


#4

def eof_error():

	while True:
		try:
			number = int(input("Input some number: "))

		except EOFError:
			print("\nEof Error!")
			break

		else:
			print("No errors!")

eof_error()


#5

def io_error():

	try:
		file = open("somefile.txt")

	except IOError:
		print("File cannot be opened")

	else:
		print("No error!")


io_error()


#6

def zero_division_error(dividend,divisor):

	try:
		result = dividend / divisor

	except ZeroDivisionError:
		print("You cannot divide a value by zero")

	else:
		print("The result is {}".format(result))


zero_division_error(10,0)


#7

def index_error(list1):

	try:
		print(list1[10])

	except IndexError:
		print("Index not found")

	else:
		print("Index in list")


sample_list = [1,2,3]
index_error(sample_list)


#8

def name_error(variable):

	try:
		print(something)

	except NameError:
		print("Variable has not been instantiated")

	else:
		print("Variable exists!")


some_string = "Hello"
name_error(some_string)


#9

def type_error(num1,num2):

	try:
		response = num1 * num2

	except TypeError:
		print("Input must be an integer")

	else:
		print("The input was a number! Congrats")
		
type_error("h1","hello")



#10

def key_error(dict1):

	try:
		print(dict1["name"])

	except KeyError:
		print("Key not found")

	else:
		print("Key is in dictionary!")

dict1 = {
	"Age": 20,
	"Address": "DC"
}

key_error(dict1)