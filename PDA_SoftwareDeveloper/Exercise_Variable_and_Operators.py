# Author : Eswari
# Description : Exercise - Variable and Operators
# Date : 06 Apr 2026


#Exercise 1: Declare two variables, x and y, and assign them values. Calculate and print the sum and difference of these two variables.
x = 10
y = 6
print(f"The sum of {x} and {y} is : {x + y}")

print(f"The difference of {x} and {y} is : {x-y}")

#Exercise 2: Create a program that calculates the area of a rectangle. Prompt the user to enter the length and width of the rectangle, 
#store these values in variables, and then calculate and display the area.  Area = length * width.
length = float(input('Enter length of the Rectangle1: '))
width = float(input('Enter width of the Rectangle1: '))
print(f"Area of the Rectangle is : {length * width:.2f}")

###Another method until user input valid input
while True:
    try:
        length = float(input('Enter length of the Rectangle2: '))
        width = float(input('Enter width of the Rectangle2: '))
        print(f"Area of the Rectangle is : {length * width:.2f}")
        break
    except ValueError as er:
        print("please enter valid number: ", er)


#Exercise 3: Create a program that converts temperatures from Fahrenheit to Celsius. 
#Prompt the user to enter a temperature in Fahrenheit, store it in a variable, and 
#then calculate and display the equivalent temperature in Celsius using the formula: Celsius = (Fahrenheit - 32) * 5/9.
temp_fahrenheit = float(input('Enter temperature in Fahrenheit: '))
temp_Celsius = (temp_fahrenheit - 32) * 5/9

print(f"The temperature in Celsius is {temp_Celsius:.2f}")


#Exercise 4:Ask the user to enter their first name and last name separately. 
#Store these values in two variables and then display a greeting message using these variables.
first_name = input("Enter the First name: ")
last_name = input("Enter Last name: ")
print(f"Welcome {first_name} {last_name} to python learning journey")
