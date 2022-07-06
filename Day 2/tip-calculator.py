# -*- coding: utf-8 -*-
"""
Name: tip-calculator.py
Author: Ashley Emetarom
Version: 1.0 (July 6, 2022)
Purpose: Takes an amount and calculates the price each person has to pay, tip
included.

Variables

float totalBill - the total amount of the bill before tip
num people - amount of people to divide the bill by
float tipAmount - the percentage of tip to be added to the bill
float total - the total bill plus the tip
float totalSplit - The final total each person needs to pay

"""

print("Welcome to the tip calculator!")

totalBill = float(input("What was the total bill? $"))
tipAmount = int(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))

tipAmount /= 100
total = totalBill + (totalBill * tipAmount)
totalSplit = round((total / people), 2)

print(f"Each person should pay ${totalSplit}.")

