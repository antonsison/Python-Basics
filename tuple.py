#1

def add_item(tuple1, add_value):

	tuple1 = tuple1 + (add_value,)

	return tuple1

sample_tuple = (1,2,3,4)
print(add_item(sample_tuple, 5))


#2

def remove_item(tuple1, remove_value):

	new_list = list(tuple1)
	new_list.remove(remove_value)

	tuple1 = tuple(new_list)
	return tuple1

sample_tuple = (1,2,3,4)
print(remove_item(sample_tuple, 4))


#3

def tuple_to_string(tuple1):

	new_string = "".join(i for i in tuple1)

	return new_string

sample_tuple = ('h','e','l','l','o')
print(tuple_to_string(sample_tuple))


#4

def assign_to_variable(tuple1):

	# Number of variables must be equal to number of elements in tuple
	num1, num2, num3 = tuple1

	print (num1)
	print (num2)
	print (num3)

sample_tuple = (1,2,3)
assign_to_variable(sample_tuple)


#5

def check_if_exists(tuple1, input1):

	for i in tuple1:
		if input1 in tuple1:
			return True

		else:
			return False

sample_tuple = (1,2,3)
print(check_if_exists(sample_tuple,1))


#6

def  tuples_to_dict(list_of_tuples):

	new_dict = {}

	for dict_key, dict_values in list_of_tuples:
		new_dict.setdefault(dict_key, []).append(dict_values)

	return new_dict


sample_list = [('x', 20), ('y', 30), ('z', 40), ('x', 10)]
print(tuples_to_dict(sample_list))

#7

def get_count(tuple1):
	new_list = []
	for i in tuple1:
		count = tuple1.count(i)
		if i not in new_list:
			new_list.append(i)
			format1 = "The value {} can be found {} times in the tuple".format(i, count)
			print(format1)


sample_tuple = (1,1,1,3,4,5,6,2,2,3,4)
get_count(sample_tuple)


#8

def sort_tuple_in_list(sample):

	sample = sorted(sample, key=lambda i: i[1], reverse=False)

	return sample


sample_list = [('item1', 24.5), ('item2', 15.10), ('item3', 12.20)]
print(sort_tuple_in_list(sample_list))


#9

def remove_empty_tuples(list1):


	list1 = [i for i in list1 if i]

	return list1


sample_list = [(), (), ('a', 'b', 'c'), ('d', 'e', 'f')]

print(remove_empty_tuples(sample_list))


#10

def show_tuple(tuple1):

	for i in tuple1:
		print(1, end=",")

sample_tuple = (1,2,3,4)
show_tuple(sample_tuple)