""" I learnt that it takes the value that was given outside the function
over the value given inside the function as shown below. """


def testing(yas=True):
    if yas:
        print("Yas")
    else:
        print("no")


cool = "Hi" == "Hi"
uncool = "smartness" == "Jack"
testing(cool)
testing(uncool)
