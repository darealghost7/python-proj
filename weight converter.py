# weight converter
FirstName = input("Enter your name:")
IdNumber = input("Enter your Id number:")
Mass = float(input("Enter your mass:"))
Height = float(input("Enter your height:"))

BMI = Mass / Height**2

if BMI < 18.5:
    print(f"{FirstName} is underweight")
elif 18.5 <= BMI <= 24.9:
    print(f"{FirstName} is Healthy weight")
elif 25 <= BMI <= 29.9:
    print(f"{FirstName} Overweight")

else:
    print("Obese")

