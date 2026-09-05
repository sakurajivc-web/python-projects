#A program that generates a raondom number, comparing to the user's number input to see which is higher.

## UTILITY Functions

# Imports /

import random
import time

# Header /
def header():
    print()
    print('————————————————————————————————————————')
    print()
    
# If input is invalid /
def invalid_input():
    print()
    print('—-Invalid input! Please retry.——')
        
## INPUT Functions 

# User's Number /
def user_number_input():
    print('Enter a Number [1-10]:')
    while True:
        try:
            get_number = int(input('-> '))
            if get_number < 1 or get_number > 10:
                invalid_input()
            else:
                return get_number
        except ValueError:
            invalid_input()
            
## PROCESSING + OUTPUT Functions

# Generate Rnadom Number /
def generated_random_num():
    generated_num = random.randint(1, 10)
    
    print()
    print('Generating Shield Number..')
    time.sleep(0.4)
    print()
    print(random.randint(1, 10), '...')
    time.sleep(0.65)
    print(random.randint(1, 10), '...')
    time.sleep(0.65)
    print(random.randint(1, 10), '...')
    time.sleep(0.65)     
    print()
    print('Shield Number:', generated_num)   
    
    return generated_num

# Compare Numbers / 
def compare_numbers(your_number, generated_number):
    if your_number > generated_number:
        return 'Your number is higher!'
    elif your_number == generated_number:
        return 'Wow, what a coincidence!'
    elif your_number < generated_number:
        return 'Your number is lower.'
        
# Try again?
def return_menu():
    print()
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
            
# Manager /
def simulate_number_shield():
    header()
    print('     N U M B E R   S H I E L D')
    header()
    
    your_number = user_number_input()
    
    generated_number = generated_random_num()
    
    message = compare_numbers(your_number, generated_number)
    
    print(message)
    print()
    
## -- MAIN PROGRAM -- ##
while True:
    simulate_number_shield()
    
    if not return_menu():
        break
header()
print('Hope you had fun!')
header()
    
