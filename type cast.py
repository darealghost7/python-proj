#type casting= the process of converting a var from one data type to another data type
   #   str() int() float() Bool ()
name = "dareal code "#e.g
age = 20
gpa = 3.2
is_student = True
gpa = int(gpa)
print(gpa)

name = "daryl code "#e.g
age = 20
gpa = 3.2
is_student = True
age = float(age)
print(age)



name = "daryl code "#e.g
age = 20
gpa = 3.2
is_student = True
age = str(age)
print(type(age)) # the type function is used to prove what type it is

name = ""# this helps to check if some one has enterted their name and if they have it will return false
age = 20
gpa = 3.2
is_student = True
name = bool(name)

print(name)


number = 0
number = int(input("enter a number:"))
result = number %2
if result == 1:
    print("number is odd  ")
else:
    print("number is even")

#program to grade student resluts:
mark = int(input ("enter a mark:"))
if mark<0 :
    print ("invalid mark")
elif mark >= 75:
    print("dist")
elif mark >= 65:
    print(6)
elif mark >= 50:
    print(4)
elif mark >= 40:
    print(3)
elif mark >= 30:
    print(2)
else :
    print("you can never make it")

name = input(" Enter your name")
if name == "":
    print("Nigga enter your name")
else:
    print(f"Hello MR  {name}")