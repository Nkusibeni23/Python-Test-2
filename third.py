import random

def view_question():
    data = [['O', '0'], ['l', '1'], ['u', 'v']]
    
    random_index = random.randint(0, len(data) - 1)
    
    random_array = data[random_index]
    
    print(random_array)


view_question()
