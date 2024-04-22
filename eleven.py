import math

def display_auxiliary_data(col):
    alphabet = "ABCDEF"  
    header_line = "/|" + alphabet[:col] 
    separator_line = "-" * (col + 2) 
    print(header_line)
    print(separator_line)

def display_formation(col, row, input_number):
    alphabet = "ABCDEF" 
    for i in range(row):
        for j in range(col):
            cell_number = change_string(i * col + j + 1)
            if i * col + j + 1 == input_number:
                print("X", end="")
            else:
                print("O", end="")
        print()

def change_string(number):
    alphabet = "ABCDEF" 
    row = math.floor((number - 1) / 6) + 1
    column = (number - 1) % 6
    column_char = alphabet[column]
    cell_number = column_char + str(row)
    return cell_number

col = 5
row = 4

input_number = 8

display_auxiliary_data(col)

display_formation(col, row, input_number)
