#python calculator
operator = input("Enter a operator +,-,*,/")
num1 = float(input("enter a number"))
num2 = float(input("Enter the second number"))

if operator == "+":
    result =num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"This{operator} is not valid bro")

