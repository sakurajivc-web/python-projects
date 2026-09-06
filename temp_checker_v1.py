#A program where the temperature input of the user is checked and classified.

## Utility Functions

# Imports /
import time
import random

# Header /
def header():
    print()
    print('—————————————————————————————————————————')
    print()
    
# If Input is invalid /
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
## Input Functions

# Pick number inpout style /
def choice_input():
    print('Generate random number [1]')
    print('Manual input [2]')
    while True:
        try:
            choice = int(input('Enter choice -> '))
            if choice < 1 or choice > 2:
                invalid_input()
            else:
                return choice
        except ValueError:
            invalid_input()

# Get room temp /
def temp_input():
    while True:
        try:
            get_temp = int(input('Enter temperature -> '))
            if get_temp < -10 or get_temp > 60:
                invalid_input()
            else:
                return get_temp
        except ValueError:
            invalid_input()
            
## Processing Functions

# Choice /
def process_number(choice):
    if choice == 1:
        print('Generating..')
        time.sleep(0.6)
        print('...')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('.')
        time.sleep(1)
        return random.randint(-10, 60)
    else:
        return temp_input()
        
# Classify Temp /
def classify(temperature):
    if temperature < 10:
        message = 'Cold'
    elif temperature <= 24:
        message = 'Cool'
    elif temperature <= 34:
        message = 'Warm'
    else:
        message = 'Hot'
        
    return message
    
## Output Functions 

# Display result
def display(temperature, message):
    print('Temperature:', temperature, '°C')
    print('Status:', message)
    
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
            
## Manager Function
def check_temperature_sim():
    header()
    print('T E M P E R A T U R E   C H E C K E R')
    header()
    
    choice = choice_input()

    temperature = process_number(choice)
    
    message = classify(temperature)
    header()
    display(temperature, message)
    
## -- MAIN PROGRAM -- ##
while True:
    check_temperature_sim()
    
    if not return_menu():
        break
        
print('Thank you for using our service!')
header()        
