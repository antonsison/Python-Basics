#1

def multiple_list(sample):
	total = 1

	for i in sample:
		total *= i

	return total

sample = [1,6,7,10]

print (multiple_list(sample))


#2

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

#3