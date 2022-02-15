age = int(input("What is the patients age? "))
if age < 12:
    weight = int(input("What is the child's weight? (kg) "))
    para = weight * 10
    print("Recommend {} mg paracetamol".format(para))
else:
    print("Recommend two 500 mg paracetamol tablets")
