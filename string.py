#1

def calculate_length(sample):
	counter = 0
	for char in sample:
		counter += 1
	return counter

	#or return len(sample)

sample = "Hello"
print (calculate_length(sample))


#2 

def counting_letters(word):
	dict = {}

	for i in word:
		keys = dict.keys()
		if i in keys:
			dict[i] += 1

		else:
			dict[i] = 1
	return dict

word = "gooooooooogggggglllleeeee"
print(counting_letters(word))

#3

def find_longest_word(words_list):
    word_len = []

    for n in words_list:
        word_len.append((len(n), n))     
    word_len.sort()
    return word_len[-1][1]

words = ["Hello", "pneumonoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialidocious"]

print(find_longest_word(words))

#4

def simple_greetings(name, age):
	
	return print("Hello, my name is {}. I am {} years old".format(name,age))

name = 'Anton'
age = 20
simple_greetings(name, age)

#5

def comma_separator(number):
		print("Original Number: ", number)
		print("Formatted Number: {:,}".format(number))

sample_num = 10000000
comma_separator(sample_num)

#6

def mmr_calculator():
	mmr = int(input("What is your current mmr?"))
	result = input("Did you win? (Y or N) ")

	if result == 'y' or result == 'Y':
		mmr += 25
		print ("Since you won, your mmr is now ", mmr)
	elif result == 'n' or result == 'N':
		mmr -= 25
		print ("Since you lost, your mmr is now ", mmr)

mmr_calculator()

#7

def strip_letters(phrase, char):
	print ("".join(i for i in phrase if i not in char))


strip_letters("This is a random phrase", "aeiou")


#8

def reverse_words(phrase):

	for i in phrase.split():
		return(" ".join(phrase.split()[::-1]))

print(reverse_words("A not so random phrase"))

#9

def letter_casing(phrase):
	case = input("Do you want to upper or lower your case? (Upper or Lower) ").lower()

	if case == 'upper':
		print(phrase.upper())
	elif case == "lower":
		print(phrase.lower())


phrase = "A Random PHRASE"
letter_casing(phrase)

# 10

def sting_to_list(phrase):
	return phrase.split(' ')


phrase = "A phrase that will become a list"
new_list = sting_to_list(phrase)

print (new_list)