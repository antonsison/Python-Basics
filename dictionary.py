#1

def iterate_dict(sample):
	for dict_key, dict_value in sample.items():
		print(dict_key + " -- " + str(dict_value))

some_dict = {'Name': 'Anton', 'Age': 20}
iterate_dict(some_dict)

#2

def update_dict(sample_dict, add_dict):
	container = {}

	for dict_key, dict_value in add_dict.items():
		container[dict_key] = dict_value
		sample_dict.update(container)

	return sample_dict

dict1 = { 'A': "Hello", 'B': "Hi" }
dict2 = { 'C': "Yow", 'D': "Hommie" }
print(update_dict(dict1, dict2))

#3

def  check_key(sample_input, dict_sample):

	if sample_input in dict_sample:
		print("Key is present in the dictionary")
	else:
		print("Key is not present in the dictionary")

dict_sample = {1,2,3,4,5,6}
check_key(9, dict_sample)


#4

def multiply_by_itself():

	number = int(input("Input a number: "))
	sample_dict = {}

	for i in range(1, number + 1):
		sample_dict[i] = i*i

	print(sample_dict)

multiply_by_itself()



#5

def get_number():
	name = input("What is your name? ")
	number = int(input("What's your number? "))

	info = {}
	info[name] = [number]

	again = True
	while again == True:
		response = input("Do you have another number? (Y or N)").lower()

		if response == 'y':
			number = int(input("What's your other number? "))
			info[name].append(number)

		elif response == 'n':
			again = False

		else:
			print("Answer only with Y or N!!")


	for dict_key, dict_value in info.items():
			string_number = dict_value
			if len(string_number) == 1:
				string_number = "".join(str(x) for x in string_number)
				format1 = "You've met a person named {} and has a phone number of ".format(dict_key) + string_number
				print(format1)
			elif len(string_number) == 2:
				string_number = " and ".join(str(x) for x in string_number)
				format1 = "You've met a person named {} and has a phone numbers of ".format(dict_key) + string_number
				print(format1)

			elif len(string_number) > 2:
				string_number = ", ".join(str(x) for x in string_number)
				format1 = "You've met a person named {} and has a phone numbers of ".format(dict_key) + string_number
				print(format1)
			

get_number()

#6

ddef get_age():
	name = input("What is your name? ")
	age = int(input("How old are you? "))

	info = {}
	info[name] = age

	again = True
	while again == True:
		response = input("Would you like to add another person? (Y or N)").lower()

		if response == 'y':
			name = input("What is his/her name? ")
			age = int(input("How old is he/she? "))
			container = {}
			container[name] = age
			info.update(container)

		elif response == 'n':
			again = False

		else:
			print("Answer only with Y or N!!")


	for dict_key, dict_value in info.items():
		format1 = "You've met a person named {} and is {:d} yrs old".format(dict_key,dict_value)
		print(format1)


get_age()


#7

def combine_dict(dict1, dict2):

	new_dict = {}

	for i in (dict1, dict2):
		new_dict.update(i)

	return new_dict

dict1 = {1:2, 3:4, 5:6}
dict2 = {7:8, 9:10, 11:12}

print(combine_dict(dict1, dict2))


#8

def keys_and_values(keys, values):

	new_dict = dict(zip(keys,values))

	return new_dict

sample_keys = ['a','b','c']
sample_values = [1,2,3]

print(keys_and_values(sample_keys,sample_values))


#9

def find_match(dict1, dict2):

	for (dict_key, dict_value) in set(dict1.items()) & set(dict2.items()):
		format1 = "{} : {} is present in both dictionaries".format(dict_key, dict_value)
		print(format1)

dict1 = {1:2, 2:4, 3:6, 4:8}
dict2 = {1:2, 2:4, 7:9, 11:12}

find_match(dict1,dict2)


#10

def find_passed(students):
	students_passed = (sum(i['passed'] for i in students))
	return students_passed



student = [ 
{'id': 1, 'name': 'Anton', 'passed': True},
{'id': 2, 'name': 'Inaki', 'passed': False},
{'id': 3, 'name': 'Sison', 'passed': True} ]

print(find_passed(student))