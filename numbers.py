#1
def reduce_tax(salary):
	tax = salary * 0.20 #20% Tax
	salary = salary - tax
	print (salary)

reduce_tax(20000) #16k

#2
def calculate_area(height,width):
	area = height * width
	print (area)

calculate_area(30,60)

#3
def get_total_list(number):
	print(sum(number))

sample = [5,10,20,30,50]
get_total_list(sample)


#4

def max_of_three( x, y, z ):
    def max_of_two( x, y ):
	    if x > y:
	        return x
	    else:
	    	return y
    return max_of_two( x, max_of_two( y, z ) )

print(max_of_three(3, 6, -5))


#5

def unique_list(sample):
	container = []

	for i in sample:
		if i not in container:
			container.append(i)
	return container

phrases = [1,1,1,1,"apple", "orange", "apple"]
print (unique_list(phrases))


#6

def get_even(number):
	container = []

	for i in number:
		if i % 2 == 0:
			if i not in container:
				container.append(i)
	return container

sample = [1,2,2,3,4,5,6,6,8,9,10]

print (get_even(sample))


#7

def get_factorial(number):
	if number == 0:
		return 1
	return number * get_factorial(number - 1)

number = 5
print (get_factorial(number))


#8

def all_exponent(number):
	container = dict()

	for i in number(range(1, number+1)):
		container[i] = i * i

	return container

number = 10
print (all_exponent(number))


#9

def odd_or_even(numbers):
	count_odd = 0
	count_even = 0
	for i in numbers:
		if i % 2 == 0:
			count_even+=1
		else:
			count_odd+=1

	print("Number of even numbers :",count_even)
	print("Number of odd numbers :",count_odd)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_or_even(numbers)

#10

def count_digits_letters(sample):
	digits = 0
	letters = 0

	for i in sample:
		if i.isdigit():
			digits += 1
		elif i.isalpha():
			letters += 1

	print ("Letters: ", letters)
	print ("Digits: ", digits)


sample = "w0w0w33"
count_digits_letters(sample)