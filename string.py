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

