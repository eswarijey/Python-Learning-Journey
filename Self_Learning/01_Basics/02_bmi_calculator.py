# Author : Eswari
# Description : BMI Calculator
# Date : 07 Apr 2026

def bmical(w,h):
    bmi = w / (h ** 2)
    return bmi

def bmicateg(bmival):
    if bmival < 18.5:
        category = "Underweight"
    elif bmival<25:
        category = "Normal"
    elif bmival<30:
        category = "Overweight"
    else:
        category = "Obese"
    return category

while True:
    try:
        weight = float(input("Enter weight in kg: "))
        if not(0<weight<=300):
            print("Invalid weight entered, the weight should from greater than 0 kg and should be less than or equal to 300 kg")
            continue

        height = float(input("Enter height in meters: "))
        if not(0<height<=2.5):
            print("Invalid height entered, the height should be greater than 0m and less than or equal to 2.5m")
            continue

        getbmi = bmical(weight,height)
        getcateg = bmicateg(getbmi)

        print(f"Your BMI is : {getbmi:.2f}")
        print("Category: ", getcateg)

        break
    
    except ValueError as ve:
        print("Error :", ve)