#A program where the user can choose a target number that must be hit by the rolled dice number.

## Utility Functions

import time
import random

# Header /
def header():
    print()
    print('———————————————————————————————————————————————')
    print()

# If input is invalid /
def invalid_input():
    print()
    print('——Invalid input! Please retry.——')
        
## INPUT Functions

# Target hit /
def target_hit_input():
    print('Hi!')
    time.sleep(1)
    print('Choose your target: [2-12]')
    while True:
        try:
            get_target = int(input('-> '))
            if get_target < 2 or get_target > 12:
                invalid_input()
            else:
                return get_target
        except ValueError:
            invalid_input()
            
## PROCESSING + OUTPUT Functions

# Roll Dice/
def roll_dice():
    print()
    print('Rolling...')
    time.sleep(1)
    dice_1 = random.randint(1, 6)
    print('Dice 1:', dice_1)
    time.sleep(0.6)
    dice_2 = random.randint(1, 6)
    print('Dice 2:', dice_2)
    time.sleep(0.6)
    
    return dice_1, dice_2
    
# Check Target/
def check_rolls(target_roll, dice_1, dice_2):
    total_hit = dice_1 + dice_2
    if total_hit == target_roll:
        message = 'Target Hit!' 
    else:
        message = 'You missed.' 
    return message, total_hit
    
# Display Result
def display_result(total_roll, target_roll, message):
    print()
    print('Total:', total_roll)
    time.sleep(1)
    print()
    print('Target:', target_roll)
    time.sleep(1)
    print(message)
    print()
    
# Manager Function
def simulate_rolls():
    header()
    print('   D I C E   T A R G E T   S I M U L A T O R')
    header()
    
    target_roll = target_hit_input()
    
    dice_1, dice_2 = roll_dice()
    
    message, total_roll = check_rolls(target_roll, dice_1, dice_2)
    
    display_result(total_roll, target_roll, message)
    
# Try again?
def return_menu():
    print('Would you like to try again?')
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
            
## MAIN PROTGRAM ##
while True:
    simulate_rolls()
    
    if not return_menu():
        break

print('Hope you had fun!')
header()