import json
import os
import csv

os.chdir('/home/anton/Desktop/scripts/Files')


#1

def write_file(data, file_name):
	with open(file_name, 'w+') as f:
		json.dump(data, f)

sample_data = {
	"Name": "Anton",
	"Age": 20,
	"Address": "Davao City"
}

write_file(sample_data, "sample.json")


#2

def append_file(data, file_name):
	with open(file_name, 'a+') as f:
		json.dump(data, f)

sample_data = {
	"Name": "Sison",
	"Age": 23,
	"Address": "Davao City"
}

append_file(sample_data, "sample.json")


#3

def read_file(file_name):
	with open(file_name, 'r') as f:
		data = json.load(f)
		print (data)

read_file("sample.json")


#4

def store_into_list(file_name):
	new_list = []
	with open(file_name, 'r') as f:
		for line in f:
			new_list.append(line)
	return new_list

print(store_into_list("sample.json"))


#5

def list_into_file(list1,file_name):
	new_list = []
	with open(file_name, 'w+') as f:
		for i in list1:
			f.write("{}\n".format(i))

sample_list = ["Red", "Green", "Blue"]			
list_into_file(sample_list,"colors.txt")


#6

def write_string():

	file_name = input("Filename: ")
	with open(file_name, 'w+') as f:

		f.write(input("Write something to save: \n"))

write_string()


#7

def number_of_characters(number,file_name):

	with open(file_name, 'r') as f:
		contents = f.read(number)
		print(contents, end='')

number_of_characters(50, "another_sample.txt")


#8

def read_first_line(file_name):

	with open(file_name, 'r') as f:
		for line in f:
			print (line)
			break
read_first_line("another_sample.txt")


#9

def copy_file(file_name, file_copy):

	with open(file_name, 'r') as rf:
		with open(file_copy, 'w+') as wf:
			for line in rf:
				wf.write(line)
copy_file("another_sample.txt", "copy2.txt")


#10

def read_csv(file_name):

	with open(file_name, 'r') as csv_file:

		csv_reader = csv.DictReader(csv_file)

		for line in csv_reader:
			print (line)


read_csv("sample_csv.csv")

