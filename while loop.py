# while loops = will execute code while some conditions remain  true

# name = input("Enter your name : ")

# while name == "":
# print("you did not enter your name!")
# name = input("Enter your name : ")
# print(f"Hello {name}")

# using the not logical operator
# food = input("what is your fave food to eat (t to quit) :")
# while not food == "t":
# print(f"You like {food}")
# food = input("what is your fave food to eat (t to quit) : ")
# print("Bye sir")

# using the not logical operator

num = int(input("Choose a number from 1 to 10:"))

while num < 1 or num > 10:
    print(f"number is not valid {num}")
    num = int(input("Choose a number from 1 to 10:"))

print(f"You picked number{num}")


