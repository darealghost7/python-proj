num_of_items = float(input("Enter the number of items you would like to purchase: "))

ship1 = 2.99
ship2 = 1.99
ship3 = 1.49
ship4 = 0.99

if num_of_items == 1:
    print(f"Your ship charges are ${ship1}")
elif 2 <= num_of_items <= 5:
    result_ship = ship1 + (num_of_items - 1) * ship2
    print(f"Your ship charges are ${result_ship}")
elif 6 <= num_of_items <= 14:
    result_ship = ship1 + ship2*4 + (num_of_items - 5) * ship3
    print(f"Your ship charges are ${result_ship}")
elif num_of_items >= 15:
    result_ship = ship1 + ship2 * 4 + 9 * ship3 + (num_of_items - 14) * ship4
    print (f"Your ship charges are ${result_ship}")

else :
    print ("oh hell nah")

