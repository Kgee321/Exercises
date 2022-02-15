gst = 0.15
item = float(input("Enter item price: "))
add = input("Do you want to add gst or remove gst?")
if add == "add":
    total_add_gst = (item * gst) + item
    print(total_add_gst)
elif add == "remove":
    total_remove_gst = item / gst
    print(total_remove_gst)
elif add != "add" or "remove":
    add = input("Try again, either type add or remove:")


