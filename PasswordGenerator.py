"""
---About PasswordGenerator program---

This program allows its users to generate strong passwords.
we are sure that all selection processes have been performed
randomly. That's why the passwords that you will generate will be
strong. Nobody knows how many upper cases, how many lower cases,
how many special characters or how many numbers the password will
include. Because the passwords are generated with randomly selected
characters.



--AUTHOR--

ramazanozkanc@gmail.com

"""


import random

lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r"
    ,"s","t","u","v","w","x","y","z"]
uppercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r"
    ,"s","t","u","v","w","x","y","z"]

count = 0
while count < len(lowercase):
    uppercase[count] = lowercase[count].upper()
    count = count+1


numbers = ["0","1","2","3","4","5","6","7","8","9"]
specialcharacters = ["!","?","@","&","%","$","#","£","#"]

ListSelection = [numbers,specialcharacters,lowercase,uppercase]

def randomC():
    selection = ListSelection[random.randint(0,3)]
    if selection == numbers:
        return numbers[random.randint(0,9)]

    elif selection == specialcharacters:
        return specialcharacters[random.randint(0,8)]

    elif selection == lowercase:
        return lowercase[random.randint(0,24)]

    else:
        return uppercase[random.randint(0,24)]


password = ""

print("enter zero to exit.")
while True:
 NumberFromUser = int(input("Enter the length of your password(between 6-32): "))
 if NumberFromUser == 0:
    break

 if NumberFromUser >= 6 or NumberFromUser <= 32:
     i = 0
     while i < NumberFromUser:
         c = randomC()
         password = password + c
         i = i + 1
     print("\n")
     print(password)
     print("\n")

     password =""

 else:
    print("Enter an appropriate length!")