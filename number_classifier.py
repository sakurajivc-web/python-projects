#User enters a number, and the program tells them what range it belongs to.

#Utility Functions//

import random
import time

#Header-
def header():
    print()
    print('—————————————————————————————————————————————————')
    print()
    
#If input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input Functions//
def number_choice():
    print('Would you like to generate a random number?')
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
            
#Processing Functions//
def determine_number():
    if not number_choice():
        while True:
            try:
                print('Enter Number to Classify: [1-100]')
                get_num = int(input('-> '))
                if get_num < 1 or get_num > 100:
                    invalid_input()
                else:
                    return get_num
            except ValueError:
                invalid_input()
    else:
        print('Generating Random Number...')
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.7)
        print('.')
        time.sleep(0.9)        
        generated_num = random.randint(1, 100)
        return generated_num

#Classify Number
def determine_classification(number):
    if number <= 25:
        num_class = '1-25'
        num_category = 'Low'
    elif number <= 50:
        num_class = '26-50'
        num_category = 'Moderate'
    elif number <= 75:
        num_class = '51-75'
        num_category = 'High'
    else:
        num_class = '76-100'
        num_category = 'Very High'
    return num_class, num_category
    
#Output Functions//

#Show Results
def display_result(number, classification, category):
    header()
    print('  N U M B E R   C L A S S I F I C A T I O N')
    header()
    print('Number:', number)
    print()
    print('Range:', classification)
    print('Category:', category)
    header()

#Try again?
def return_menu():
    print('Would you like to check again?')
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

#Manager Function//    
def check_number():
    header()
    print('  N U M B E R   C L A S S I F Y E R')
    header()     
    number = determine_number()
    
    classification, category = determine_classification(number)
    
    display_result(number, classification, category)
    
## -- MAIN PROGRAM -- ##
while True:
    check_number()
    
    if not return_menu():
        break
        
print('Thank you for using our service')
header()