def change_input_number(input_str):
    letter_to_number = {'A': 0, 'B': 1, 'C': 2}
    
    letter, number_str = list(input_str)

    number = letter_to_number[letter]

    number = int(number_str)

    cell_number = number * 3 + number
    return cell_number

input_str = "B2"
cell_number = change_input_number(input_str)
print("Debug: input_number =", cell_number)
