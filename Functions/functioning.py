def calculate_double(amount):
    double = amount * 2
    return double


def calculate_half(amount):
    half = amount / 2
    return half


def calculate_ten_more(amount):
    ten_more = amount + 10
    return ten_more


question = int(input("How much? "))
print(f"Double {question} is: {calculate_double(question)}")
print(f"Half of {question} is: {calculate_half(question)}")
print(f"Ten more of {question} is: {calculate_ten_more(question)}")
