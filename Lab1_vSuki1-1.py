"""
UPC Validator

Author: Disukhi Ahmed


"""

# function that calculates the check digit of a valid UPC code( check digit is the last digit of the UPC)
def find_upc(first_eleven):
    # add the odd digits and multiply by 3, then add the even digits and find the total
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


# prompt the user for a 12 digit upc
UpcInput = input("Enter a 12 digit UPC code: ")

# checks length of the UPC Code, if it isnt 12 digits it is invalid, if it is the program continues
if len(UpcInput) != 12:
    print("Invalid")
else:  
    #stores the check digit into a variable
    checkDigitInput = int(UpcInput[11])

#calls the function to calculate the valid check digit, and compares it to the check digit inputted by the user, if they are equal it is valid, if not it is invalid.
    check_Digit_Calculated = find_upc(UpcInput)
    if checkDigitInput == check_Digit_Calculated:
         print("Valid")
    else: 
        print("Invalid")
        