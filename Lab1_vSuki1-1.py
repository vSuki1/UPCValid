"""
UPC Validator

Author: Disukhi Ahmed


"""


def check_upc(first_eleven):
    sum_Of_Odd = first_eleven[0] + first_eleven[2] + first_eleven[4] + first_eleven[6] + first_eleven[8] + first_eleven[10]
    sum_Of_Odd = sum_Of_Odd * 3
    