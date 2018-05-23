#1

def show_list(sample):

	for i in sample:
		print(i)

sample = [420 "Blaze", "It"]
show_list(sample)


#2

def multiple_list(sample):
	total = 1

	for i in sample:
		total *= i

	return total

sample = [1,6,7,10]

print (multiple_list(sample))


#3

def find_match(list1, list2):
	result = False
	for i in list1:
		for y in list2:
			if i == y:
				result = True
	return result

list1 = [1,3,6,7]
list2 = [2,5,6,3]

print(find_match(list1,list2))

#4

def greet_everyone(sample):
    
    for i in sample:
        print ("Hello {}".format(i))

sample = ["Anton", "Iñaki", "Sison"]
greet_everyone(sample)


#5

def list_to_string(sample_list):

	sample_list = ' '.join(sample_list)
	return sample_list



some_list = ["A", "List", "That", "Will", "Become", "A", "String"]
print(list_to_string(some_list))


#6

def combine_list(list1,list2):
	new_list = list1 + list2

	return new_list


list1 = ["Part", 1, "of", "the", "list"]
list2 = ["Part", 2, "of", "the", "list"]

print(combine_list(list1,list2))


#7

def get_letter_grade(grade):
	list_of_grades = []
	for i in grade:
		if i < 72:
			list_of_grades.append("F")
		elif i >= 72 and i < 76:
			list_of_grades.append("D")
		elif i >= 76 and i < 79:
			list_of_grades.append("C")
		elif i >= 79 and i < 84:
			list_of_grades.append("C+")
		elif i >= 84 and i < 87:
			list_of_grades.append("B")
		elif i >= 87 and i < 91:
			list_of_grades.append("B+")
		elif i >= 92:
			list_of_grades.append("A")

	return list_of_grades
	
some_list = [92,93,86,88,60,73]
print(get_letter_grade(some_list))


#8

def likes(list1):

	if not list1:
			format0 = "no one likes this"
			return format0
			
	for i in list1:
		
		if len(list1) == 1:
			format1 = "{} likes this".format(i)
			return format1

		elif len(list1) == 2:
			if i == list1[0]:
				container = i
			elif i == list1[1]:
				format2 = container + " and {} likes this".format(i)
				return format2

		elif len(list1) == 3:
			if i == list1[0]:
				container = i
			elif i == list1[1]:
				container2 = i
			elif i == list1[2]:
				format3 = container + ", " + container2 + " and {} likes this".format(i)
				return format3

		elif len(list1) >= 4:
			persons_left = str(len(list1) - 2)
			if i == list1[0]:
				container = i
			elif i == list1[1]:
				format4 = container + ", {} and ".format(i) + persons_left + " others like this"
				return format4


sample_list = ["Anton", "Inaki", "Liangco", "Sison"]
print(likes(sample_list))

#9

def  check_name(names):
	names = [i.lower() for i in names]
	check_name = input("Input name to know if student passed (Case Sensitive): ").lower()

	for i in names:
		if check_name not in names:
			format1 = "Sorry, {} could not be found in the list.".format(check_name.capitalize())
			return format1
		elif check_name in names:
			format2 = "Congratulations! {} is on the list!".format(check_name.capitalize())
			return format2


list_of_names = ["Anton", "John", "Doe", "Jane"]

print(check_name(list_of_names))

#10

def namelist(names):

	if not names:
		return 'No names found'

	for i in names:
		for dict_keys, dict_value in i.items():
			if len(names) == 1:
				return dict_value
			elif len(names) == 2:
				if i == names[0]:
					container = dict_value
				elif i == names[1]:
					format1 = container + " & " + "{}".format(dict_value)
					return format1

			elif len(names) >= 3:
				if i == names[0]:
					container = dict_value
				elif i == names[1]:
					container2 = dict_value
				elif i == names[2]:
					format1 = container + ", " + container2 + " & " + "{}".format(dict_value)
					return format1


some_list = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

print(namelist(some_list))
