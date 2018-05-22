#1 simply gets letter grade

def get_letter_grade(grade):
	if grade < 72:
		print ("F")
	elif grade >= 72 and grade < 76:
		print ("D")
	elif grade >= 76 and grade < 79:
		print ("C")
	elif grade >= 79 and grade < 84:
		print ("C+")
	elif grade >= 84 and grade < 87:
		print ("B")
	elif grade >= 87 and grade < 91:
		print ("B+")
	elif grade >= 92:
		print ("A")

get_letter_grade(92)


#2