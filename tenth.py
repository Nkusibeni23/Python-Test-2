import math

def display_formation(col, row, input_number):
    alphabet = "ABC"
    for i in range(row):
        for j in range(col):
            cell_number = change_string(i * col + j + 1)
            if i * col + j + 1 == input_number:
                print("X", end="")
            else:
                print("O", end="")
        print()

def change_string(number):
    alphabet = "ABC"
    row = math.floor((number - 1) / 3) + 1
    column = (number - 1) % 3
    column_char = alphabet[column]
    cell_number = column_char + str(row)
    return cell_number

col = 5
row = 4

input_number = 10

display_formation(col, row, input_number)
