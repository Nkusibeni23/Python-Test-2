import math

def change_string(number):
    
    alphabet = "ABC"

    row = math.floor((number - 1) / 3) + 1
    column = (number - 1) % 3

    column_char = alphabet[column]
    
    cell_number = column_char + str(row)
    return cell_number

number = 3
cell_number = change_string(number)
print("Cell Number:", cell_number)
