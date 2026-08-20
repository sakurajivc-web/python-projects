#A program that simulates the light cycle for a traffic light.

#Utility functions//

import time
import random

lights = ['RED', 'GREEN', 'YELLOW']

#Header
def header():
    print()
    print('—————————————————————————————————————————')
    print()

#If input is invalid
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
#Input Functions//

#Cycle Choice
def cycle_choice_input():
    print('Choose cycle input:')
    print('[1] — Random')
    print('[2] — Manual')
    time.sleep(1) 
    while True:
        try:
            get_choice = int(input('-> '))
            if get_choice < 1 or get_choice > 2:
                invalid_input()
            else:
                return get_choice
        except ValueError:
            invalid_input()
            
#Cycle Input
def cycle_input(cycle_choice):
    if cycle_choice == 1:
        return random.randint(1, 30)
    else:
        print('Enter Cycle Amount [1-30]')
        time.sleep(1)
        while True:
            try:
                get_amount = int(input('->'))
                if get_amount < 1 or get_amount > 30:
                    invalid_input()
                else:
                    return get_amount
            except ValueError:
                invalid_input()
                
#Processing and Output Functions//
def simulate_traffic(cycles):
    print('Cycles:', cycles)
    print()
    time.sleep(0.5)
    for cycle in range(cycles):
        light = random.choice(lights)
        
        print('Cycle:', cycle + 1)
        print('Light:', light)
        time.sleep(0.4)
        
        print('.')
        time.sleep(0.4)
        print('..')
        time.sleep(0.4)
        print('...')
        time.sleep(0.4)
        
        if light == 'RED':
            print('STOP!')
        elif light == 'YELLOW':
            print('SLOW DOWN!')
        else:
            print('GO!')
            
        time.sleep(0.5)
        print()
        
def return_menu():
    print('Would you like to simulate again?')
    print('[Y] — Yes')
    print('[N] — No')
    time.sleep(0.6)
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
def traffic_light_sim():
    header()
    print('  T R A F F I C    L I G H T    S I M')
    header()
    
    cycle_choice = cycle_choice_input()
    print()
    cycles = cycle_input(cycle_choice)
        
    simulate_traffic(cycles)
    
## -- MAIN PROGRAM -- ##
while True:
    traffic_light_sim()
    header()
    
    if not return_menu():
        break
        
print('Drive Safely!')
header()