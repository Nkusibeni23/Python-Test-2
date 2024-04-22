def start_message():
    print("Start the game!")

def section_message(level):
    print("Level:", level)

def play():
    section_message(1) 
    choice = input("Input cell number (e.g. A1) of different character: ")
    print("Debug: choice =", choice)
start_message()
play()
