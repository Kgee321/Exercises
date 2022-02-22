def say_hello(name_first, name_last):
    return f"Hello {name_first} {name_last} from a function!"


name = input("What is your name: ").strip()
other = input("What is your last name: ").strip()
print(say_hello(name, other))
