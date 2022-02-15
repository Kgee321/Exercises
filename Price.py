price = float(input("What is the Price? "))
item_type = input("What is your Item Type? ")

if price >= 10: 
    if item_type == "food":
        percentage = price * 0.6
    elif item_type == "electrical":
        percentage = price * 0.7
    else:
        percentage = price * 0.9
    print("You get a discount of ${}, \n Your price is now ${}".format(percentage, price + percentage))
else:
    print("You do not get a discount, you price is still ${}".format(price))




