num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
opp = input("select + or - or *: ")
result = 0

if opp == "+":
    result = num_1 + num_2
elif opp == "-":
    result = num_1 - num_2
elif opp == "*":
    result = num_1 * num_2

    print(num_1)
    print(num_2)

    print("result is:", result)
