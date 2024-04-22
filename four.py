import random

def display_3x3_formation():
    
    data = [['O', '0'], ['l', '1'], ['u', 'v']]
   
    random_index = random.randint(0, len(data) - 1)
    
    
    random_array = data[random_index]
    
    
    first_element = random_array[0]
    
   
    for _ in range(3):  
        line = ""  
        for _ in range(3):  
            line += first_element
        print(line)
        
display_3x3_formation()
