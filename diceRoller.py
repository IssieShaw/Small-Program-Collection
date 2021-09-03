import random
import time


def validation(msg, valid = False):
    var = 100
    while not valid:
        try:
            var = int(input(msg))
            if range_check(var, 2, 50) == var:
                return var
        except ValueError:
            print("Please enter an integer (whole number).")
            

def range_check(value, low, high):
    if low < value < high:
        return value
    else:
        print("You think you a real dice could hold these numbers? Silly.")
        return ValueError

    
def menu():
    print("Welcome to Dice!\nOnce the dice are rolling, press Enter to continue, 'm' for menu, or 'e' to exit.")
    selection = validation("\nHow many sides would you like your dice to have?\n> ")
    return selection


running = True
sides = menu()
while running:
    print("\nRolling dice...")
    time.sleep(0.5)
    print(random.randrange(1, sides + 1))
    
    selection = input("> ")
    if selection.lower() == "e":
        print("Quitting Dice!")
        running = False
    elif selection.lower() == "m":
        sides = menu()
    else:
        continue



