#A program simulating a coin flip tracker.

#Utility Functions//

import time
import random

coin_sides = ['Heads', 'Tails']

#Header
def header():
    print()
    print('———————————————————————————————————————')
    print()
    
#If input is invalid
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
#Input Functions//

#Cycle Choice
def cycle_choice_input():
    print('Choose Cycle Input Mode:')
    print('[1] — Random')
    print('[2] — Manual')
    time.sleep(0.4)
    while True:
        try:
            get_choice = int(input('-> '))
            if get_choice < 1 or get_choice > 2:
                invalid_input()
            else:
                return get_choice
        except ValueError:
            invalid_input()
            
#Cycle Amount
def cycles_amount(input_choice):
    if input_choice == 1:
        print('Generating')
        time.sleep(0.45)
        print('.')
        time.sleep(0.45)
        print('..')
        time.sleep(0.45)
        print('...')
        time.sleep(0.45)
        return random.randint(1, 20)
    else:
        print('Enter Cycles Amount [1-20]', end='')
        time.sleep(0.4)
        while True:
            try:
                get_amount = int(input('-> '))
                if get_amount < 1 or get_amount > 20:
                    invalid_input()
                else:
                    return get_amount
            except ValueError:
                invalid_input()
                
#Processing and Output Functions

#Simulate Flips
def flip_coin(cycles):
    
    heads = 0
    tails = 0
    
    print('Cycles:', cycles)
    print()
    time.sleep(0.5)
    print('Flipping...')
    time.sleep(1)
    print()
    
    for flips in range(cycles):
        flip = random.choice(coin_sides)
        print('Flip', flips + 1, '=', flip)
        time.sleep(1)
        if flip == 'Heads':
            heads += 1
        elif flip == 'Tails':
            tails += 1
        
    header()
    print('   T O T A L   F L I P S')
    header()
    print('Heads:', heads)
    print('Tails:', tails)
    header()
    
#Try again?
def return_menu():
    print('Would you like to try again? ')
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

#Manager Functions
def simulate():
    header()
    print('   C O I N   F L I P P E R')
    header()
    input_choice = cycle_choice_input()
    print()
    cycles = cycles_amount(input_choice)
    header()
    flip_coin(cycles)
    
## -- MAIN PROGRAM -- ##
while True:
    simulate()
    
    if not return_menu():
        break
        
print('Thanks for playing!')
header()