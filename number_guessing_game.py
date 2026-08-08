#A program simulating a guessing game where the user guesses the number selected by the program until they get it right.
import random

#Utility Functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————')
    print()
    
#if input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')

#Random number generator function
def generate_number():
    generated_number = random.randint(1, 100)
    return generated_number
    
#Input Function//

#Pick a number
def get_guess_number():
    print()
    print('——————————————————————————————————————————')
    print('      N U M B E R   G U E S S I N G')
    print('——————————————————————————————————————————')
    print()
    while True:
        try:
            get_number = int(input('-> '))
            if get_number < 1 or get_number > 100:
                invalid_input()
            else:
                return get_number
        except ValueError:
            invalid_input()
            
#Processing Functions//

#Check the guess
def check_guess(guessed_number, secret_number):
    if guessed_number < secret_number:
        return 'Guess Higher!'
    elif guessed_number == secret_number:
        return 'Congratulations! you guessed the number!', '[', secret_number, ']'
    else:
        return 'Guess Lower!'
        
#Output Functions//

#Guess the number
def play_game():
    secret_number = generate_number()
    while True:
        guessed_number = get_guess_number()
    
        message = check_guess(guessed_number, secret_number)
        print(message)
        header()
        
        if guessed_number == secret_number:
            break
            
#Play again?
def return_menu():
    print('Would you like to play again?')
    print('[Y] — Yes')
    print('[N] — No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == '':
            invalid_input()
        elif choice == 'Y' or choice == 'YES':
            return True
        elif choice == 'N' or choice == 'NO':
            return False
        else:
            invalid_input()
            
## -- MAIN PROGRAM -- ##
while True:
    play_game()

    if not return_menu():
        break
        
header()        
print('Thank you for playing!')
header()




