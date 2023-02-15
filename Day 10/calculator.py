""" 
Name: Basic Calculator
Version: 1.0
Author: @aemetarom
Purpose: Performs basic arithmetic on two numbers and allows user to pick which operation to use.

Variables:
dict operations - Dictionary of operators and associated function names for calculation
bool should_continue - Flag for continuing calculations
float num1 - First operand for calculation
float num2 - Second operand for calculation
str operation_symbol - String representation of calculation to be performed
func calculation_function - Function to be used for the selected calculation
float answer - Result of the calculation
str continue_calculation - String check for whether the calculation should continue with the previous result,
start a new calculation, or exit the program

Functions:
calculator(): The main calculator program
float add(n1,n2): Function for performing addition
float subtract(n1,n2): Function for performing subtraction
float multiply(n1,n2): Function for performing multiplication
float divide(n1,n2): Function for performing division 
"""

# Modules

from art import logo
from os import system

# Functions

# Add
def add(n1,n2):
    return n1 + n2
    
# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'e' to exit: ").lower()
        if continue_calculation == "y":
            num1 = answer
        elif continue_calculation == "n":
            should_continue = False
            system("cls")
            calculator()
        else:
            should_continue = False

calculator()