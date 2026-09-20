"""
UPC Validator

Author: Disukhi Ahmed


"""


def find_upc(first_eleven):
    sum_Of_Odd = first_eleven[0] + first_eleven[2] + first_eleven[4] + first_eleven[6] + first_eleven[8] + first_eleven[10]
    sum_Of_Odd = sum_Of_Odd * 3
    sum_Of_Even = first_eleven[1] + first_eleven[3] + first_eleven[5] + first_eleven[7] + first_eleven[9]
    total = sum_Of_Odd + sum_Of_Even
    m = total % 10
    if m == 0:
        check_digit = 0
        else: 
            check_digit = 10 - m
    return check_digit



    UpcInput = input("Enter a 12 digit UPC code:")

    checkDigitInput = int(UpcInput[11])

    check_Digit_Calculated = find_upc(UpcInput)
