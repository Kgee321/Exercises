price = float(input("What is the Price? "))
item_type = input("What is your Item Type? ")

if price >= 10: 
    if item_type == "food":
        percentage = price * 0.6
    elif item_type == "electrical":
        percentage = price * 0.7
    else:
        percentage = price * 0.9
    pp = price + percentage
    print(f"You get a discount of {percentage}%, \nYour price is now ${pp:,.2f} (2dp)")
else:
    print(f"You do not get a discount, you price is still ${price:,.2f} (2 dp)")




