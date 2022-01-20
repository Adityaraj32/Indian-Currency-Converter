'''
Author: Adityaraj Yadav 
Date: 20 January 2022
Project Name: Indian Currency Converter
Purpose:For Practising Purpose
'''

print("\n\t\t\t\t\t\tWelcome to the Currency Converter!!!\n")

# Retriving the data from the Currency_Data.txt in which the data of Currency is Stored
with open("Currency_Data.txt") as f:
    Data = f.readlines()

# Making an Dictionary in which we will store the data of Currency_Data.txt
Currency_Dict = {}

# Spliting the data of Currency_Data.txt because the last row is not in use
for item in Data:
    data = item.split(" ")
    Currency_Dict[data[0]] = data[1]

amount = int(input("Enter the amount of money in Indian Currency: "))

print("\nTo which currency do you want to convert the available options are listed below??")

# printing the keys of the dictionary as how much data we have
[print("\t",item) for item in Currency_Dict.keys()]

To_Currency = input("\nEnter the Current to which you want to Convert: ")

# Printing and Calculating the Converstion of the currency 
print(
    f"\n\t{amount} INR in {To_Currency} is equal to {amount*float(Currency_Dict[To_Currency])}")