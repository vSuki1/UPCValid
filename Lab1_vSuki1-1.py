"""
UPC Validator

Author: Disukhi Ahmed


"""


def find_upc(first_eleven):
    sum_Of_Odd = int(first_eleven[0]) + int(first_eleven[2]) + int(first_eleven[4]) + int(first_eleven[6]) + int(first_eleven[8]) + int(first_eleven[10])
    sum_Of_Odd = sum_Of_Odd * 3
    sum_Of_Even = int(first_eleven[1]) + int(first_eleven[3]) + int(first_eleven[5]) + int(first_eleven[7]) + int(first_eleven[9])
    total = sum_Of_Odd + sum_Of_Even
    m = total % 10
    if m == 0:
        check_digit = 0
    else: 
        check_digit = 10 - m
    return check_digit



UpcInput = input("Enter a 12 digit UPC code: ")

if len(UpcInput) != 12:
    print("Invalid")
else:  
    checkDigitInput = int(UpcInput[11])

    check_Digit_Calculated = find_upc(UpcInput)
    if checkDigitInput == check_Digit_Calculated:
         print("Valid")
    else: 
        print("Invalid")