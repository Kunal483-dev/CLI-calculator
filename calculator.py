# User se input lena
num1 = float(input("Pehla number dalein: "))
operator = input("Operator dalein (+, -, *, /): ")
num2 = float(input("Doosra number dalein: "))

# Calculation aur result
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Zero se divide nahi kar sakte!")
else:
    print("Invalid operator!")
