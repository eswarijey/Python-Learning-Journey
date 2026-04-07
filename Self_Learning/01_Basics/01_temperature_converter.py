# Author : Eswari
# Description : Temperature Converter (Convert Fahrenheit <-> Celsius)
# Date : 07 Apr 2026

def FToC(fahr):
    temp_cels = (fahr - 32) * 5/9
    return temp_cels

def CToF(cels):
    temp_fahr = (9/5) * cels + 32
    return temp_fahr

mapping_option = {1:1, 2:2}
print(mapping_option)
while True:
    try:
        print('Enter option number for Temperature conversion\n')
        get_option = int(input("1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n"))
        print(f"you have entered Option {get_option}")
        if get_option in mapping_option:
            
            match get_option:
                case 1:
                    result = FToC(float(input("Enter Fahrenheit: ")))
                    print(f"Celsius: {result:.2f}")

                case 2:
                    result = CToF(float(input("Enter Celsius: ")))
                    print(f"Fahrenheit: {result:.2f}")
            break
        else:
            print('Invalid Input, Enter 1 or 2')
    except ValueError as ve:
        print("Error message :", ve)
