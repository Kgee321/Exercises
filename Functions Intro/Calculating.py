def calculate_double(amount):
    double = amount * 2
    return double


question = int(input("How much? "))
print(f"Double {question} is: {calculate_double(question)}")
calculate_double(question)
