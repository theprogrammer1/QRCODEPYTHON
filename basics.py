num1 = float(input("Please enter the first number: "))
op = input("Please enter operator: ")
num2 = float(input("Please enter the secind number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


