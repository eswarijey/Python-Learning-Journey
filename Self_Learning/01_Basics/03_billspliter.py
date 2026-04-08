# Author : Eswari
# Description : Bill Splitter
# Date : 08 Apr 2026

def cal_splitamount(totalbill, noofpeople, tippercentage ):
    tip_amount = totalbill * (tippercentage/100)
    tot_with_tip = totalbill + tip_amount
    split_amount = tot_with_tip / noofpeople
    print("====Bill Summary=====")
    print(f'Total bill amount: £{totalbill}')
    print(f'Tip percentage {tippercentage}% amount: £{tip_amount}')
    print(f'Total bill amount with tip: £{tot_with_tip}')
    print(f'Split amount for each person: £{split_amount:.2f}')
    print("======================")
    
def get_inputs():
    while True:
        try:
            totalbill = float(input("Enter Total bill amount: "))
            if totalbill < 0:                                          # Avoid negative values
                print("Total bill amount should be greater than 0")   
                continue
            
            noofpeople = int(input("Enter number of people to split the bill: "))
            if noofpeople < 1:                                                # Avoid negative values and Zero  
                print("Number people should be greater than or equal to 1")    
                continue

            tippercentage = float(input("Enter Tip percentage: "))   # Avoid negative values
            if tippercentage < 0:
                print("Percentage cant be less than zero")
                continue

            break
        except ValueError as ve:
            print("Error: ",ve)
    return totalbill, noofpeople, tippercentage

def main():
    "Main function to run Bill Spliter"
    print("====Welcome to Bill Spliter====\n")
    totalbill, noofpeople, tippercentage = get_inputs()
    cal_splitamount(totalbill, noofpeople, tippercentage)

if __name__ == "__main__":
    main()