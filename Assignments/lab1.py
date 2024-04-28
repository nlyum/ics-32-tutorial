# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Nathan Lyum
# nlyum@uci.edu
# 63833693

def calculate(oper1, oper2, operator):
    result = 0
    if operator == "+":
        result = oper1 + oper2
    elif operator == "-":
        result = oper1 - oper2
    elif operator == "x":
        result = oper1 * oper2

    return result

if __name__ == "__main__":
    print("Welcome to ICS 32 PyCalc!\n")
    operand_1 = int(input("Enter your first operand: "))
    operand_2 = int(input("Enter your second operand: "))
    
    operator = ''
    while operator not in ("+", "-", "x"):
        operator = input("Enter your desired operator (+, -, or x): ")

    result = calculate(operand_1, operand_2, operator)
    print(f"The result of your calculation is: {result}")
