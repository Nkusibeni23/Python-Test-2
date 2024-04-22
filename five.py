import random

def display_diff_element_3x3_formation():
    data = [['O', '0'], ['l', '1'], ['u', 'v']]
    
    random_index = random.randint(0, len(data) - 1)
    random_array = data[random_index]
    
    first_element = random_array[0]
    second_element = random_array[1]
    
    random_index = random.randint(0, 8)
    
    for i in range(9):
        if i == random_index:
            print(second_element, end='')
        else:
            print(first_element, end='')
        if (i + 1) % 3 == 0:
            print()  

display_diff_element_3x3_formation()
