def is_correct_number(mistake_number, input_number):
    return mistake_number == input_number

def view_result(is_correct):
    if is_correct:
        print("Correct!")
    else:
        print("Wrong")
