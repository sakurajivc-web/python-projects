#A program simulating an even or odd number checker where the user can input a number or ask the programn to generate a random number.

#Utilities

import time
import random
import sys

#Header
def header():
    print()
    print('——————————————————————————————————————————————————————————————')
    print()
    
#If input is invalid
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
#Input Functions
def number_choice():
    print('Would you like to input a number or Generate a Random Number?')
    print('[1] — Manual Input')
    print('[2] — Randomizer')
    while True:
        try:
            get_choice = int(input('-> '))
            if get_choice < 1 or get_choice > 2:
                invalid_input()
            else:
                return get_choice
        except ValueError:
            invalid_input()
            
#Processing Functions

#Number processing
def process_choice(choice):
    if choice == 1:
        while True:
            try:
                print('Enter a Number: [No Negative Integers]')
                get_number = int(input('-> '))
                if get_number < 1:
                    invalid_input()
                else:
                    return get_number
            except ValueError:
                invalid_input()
    elif choice == 2:
        print('Generating Random Number...')
        print('.')
        time.sleep(0.5)
        print('..')
        time.sleep(0.7)
        print('...')
        time.sleep(0.9)
        generated_num = random.randint(1, sys.maxsize)
        return generated_num

#Check if num is odd or even
def check_type(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd' 
     
#Output Functions//

#Show results
def display_results(number, type):
    time.sleep(1)
    header()
    print('                    R  E  S  U  L  T  S')
    header()
    
    print('Number:', number)
    print('Classification:', type)
    
    header()
    
#Check again?
def return_menu():
    print('Would you like to check again?')
    print('[Y] — Yes')
    print('[N] — No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == '':
            invalid_input()
        elif choice == 'YES' or choice == 'Y':
            return True
        elif choice == 'NO' or choice == 'N':
            return False
        else:
            invalid_input()
            
#Manager Function//
def simulate_checker():
    header()
    print('        E V E N    O R    O D D    C H E C K E R')
    header()
    
    choice = number_choice()
    print()
    
    number = process_choice(choice)
    type = check_type(number)
    
    display_results(number, type)
    
## -- MAIN PROGRAM -- ##
while True:
    simulate_checker()
    
    if not return_menu():
        break

print('Thank you for using our app.')
header()            
#END OF PROGRAM