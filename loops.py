#1 Simple for loop
list = [1, 2, 3 , 4, 5]

for i in list:
	print (i)
print("\n\n")

    
#2 Simple While
b = 10
while b > 0:
    print (b, end=' ')
    b = b - 1
print("\n\n")

#3
names = ["King", "LeBron", "James"]
for i in range(1, len(names)):
    print(names[i])
print("\n\n")


#4
for i in range(0, 11):
    if i % 2 == 0:
        print("Number ", i, " is even")

    else:
        print("Number ", i, " is odd")

print("\n\n")


#5
x = False
while x != True:
    for i in range(1,101):
        if i == 50:
            print ("Half")
        elif i == 100:
            print ("Complete")
            x = True
print("\n\n")


#6
sample = [3,2,4,5,1,6,10,20,30]
for i in sample:
    while i > 1:
        print (i)
        break
    if i == 1:
        print("it\'s da one")
print("\n\n")


#7
some_number = 20

while some_number > 0:
    if some_number > 15:
        print (some_number)
    some_number = some_number - 1
print("\n\n")


#8
person = ["Worker", "Neet", "Player", "Boss"]

for i in person:
    print (i, end=",")
print("\n\n")


#9
money = 0

while money < 1000:
    print ("Work to earn 250")
    money += 250
    if money >= 1000:
        print ("No need to work anymone")
print("\n\n")

#10
grades = [92, 70, 82, 65]

for i in grades:
    if i < 72:
        print("Student failed")
    elif i >= 72:
        print("Student passed")
print("\n\n")