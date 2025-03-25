#gross calculation
employ_name = input ("enter your name : ")
hours_worked = float(input("Add your hours worked: "))
hourly_rate = float(input("Add your hourly rate: "))
over_h = float(input("Add your overtime: "))


gross = hours_worked * hourly_rate
over_time = over_h * 2 * hourly_rate
print(f"hi {employ_name}")
print(f"Your Total overtime:  R{over_time}")
print(f"Your total is :   R{gross +over_time}")


#other code chat gpt hours_worked =
#hours_worked = float(input("Add your hours worked: "))
#hourly_rate = float(input("Add your hourly rate: "))
#print(f"Your total is {hours_worked * hourly_rate}")