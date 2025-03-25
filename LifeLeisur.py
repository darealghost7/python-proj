print("The options are 1 for park view + $150000.option 2 golf course view$170000.option 3 lake view$210000")
client = input("Choose from 1,2 and condo 3: ")
car = input("Choose from a garage or a parking space:")
one = 150000
two = 170000
three = 210000
garage = 5000

if client == "1" and car == "garage":
    result_price = one + garage
    print(f"park view and garage is ${result_price}")

elif client == "2" and car == "garage":
    result_price = two + garage
    print(f"golf course ${result_price}")

elif client == "3" and car == "garage":
    result_price = three + garage
    print(f"lake view ${result_price}")

elif client == "1" and car == "parking space":
    print(f"lake view ${one} and no garage")

elif client == "2" and car == "parking space":
    print(f"golf course ${two} and no garage")

elif client == "3" and car == "parking space":
    print(f"lake view ${three} and no garage")
else:
 print("invalid code price is 0 ")


