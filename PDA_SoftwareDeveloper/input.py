# Author : Eswari
# Description : Practicing input function
# Date : 06 Apr 2026
'''
variable = input("Enter a value: ")
print(f"You entered: {variable}")

age = int(input("Enter your age: "))
print(f"You are {age+1} years old in next year.")

price = float(input("Enter the price of the item: "))
print(f"The price of the item is: {price:.2f}")

boolean_input = input("Enter True or False: ")
if boolean_input.lower() == 'true':
    boolean_value = True
elif boolean_input.lower() == 'false':
    boolean_value = False
else:
    boolean_value = None
    print("Invalid input for boolean value.")
    
'''
#Another way to get boolean input 
mapping = {'true': True, 'false': False}
while True:
    boolean_input = input("Enter True or False: ").strip().lower()
    if boolean_input in mapping:
        boolean_val = mapping[boolean_input]
        print(f"You entered: {boolean_val}")
        break
