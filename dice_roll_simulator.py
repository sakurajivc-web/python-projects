#A program that simulates rolling dices, with the amount of rolls depending on the user's input.

#Utility Functions//

import random
import time

#Header
def header():
    print()
    print('——————————————————————————————————————————————')
    print()
    
#If input is invalid
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input Function//
#Get amount of dice to roll
def roll_amount_input():
    print('Enter Amount of Dice Rolls: [1 - 10]')
    while True:
        try:
            get_amount = int(input('-> '))
            if get_amount < 1 or get_amount > 10:
                invalid_input()
            else:
                return get_amount
        except ValueError:
            invalid_input()
            
#Processing Function//
#Roll based from amount
def roll_dice(roll_amount):
    total = 0
    for roll in range(roll_amount):
        dice = random.randint(1, 6)
        print('Dice', roll + 1, ':', dice )
        time.sleep(1)
        
        total += dice
        
#Output Functions//

#Roll Results
def roll_results(roll_amount, total):
    header()
    print('Dice Rolled:', roll_amount)
    print('Total:', total)
    header()
    
#Roll again?
def return_menu():
    print('Would yoyu like to roll again?')
    print('[Y] — Yes')
    print('[N] — No')
    print('——————————————————————————————————————————————')
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
            
#Manager Function//
def simulate_roll():
    header()
    print('        D  I  C  E      R  O  L  L  E  R')
    header()
    roll_amount = roll_amount_input()
    
    print()
    print('Rolling...')
    time.sleep(1.8)
    print()
    
    total = roll_dice(roll_amount)
    
    roll_results(roll_amount, total)

## -- MAIN PROGRAM -- ##
while True:
    simulate_roll()
    
    if not return_menu():
        break