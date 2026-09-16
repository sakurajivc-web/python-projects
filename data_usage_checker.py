#A program that asks a user for their monthly internet plan and how much data they've used.

#Imports

import time 

#Utilities

def header(): #header 
    print() 
    print('——————————————————————————————————————')
    print()
    
def invalid_input(): #if input is invalid 
    print() 
    print('——Invalid Input! Retry.——')
        
#INPUT .1 
def internet_plan_name(): #get name of internet plan 
    while True: 
        print("Enter your internet plan:") 
        print('[1] Fiber 10') 
        print('[2] Fiber 25') 
        print('[3] Fiber 50') 
        try:
            user_input = int(input('-> ')) 
            if user_input < 1 or user_input > 3: 
                invalid_input() 
            else: 
                return user_input
        except ValueError:
            invalid_input()
            
#PROCESS .1 
def classify_internet_plan(internet_plan): #classify plan based return user input 
    if internet_plan == 1: 
        plan_name = 'Fiber 10' 
        plan_limit = 10 
    elif internet_plan == 2: 
        plan_name = 'Fiber 25' 
        plan_limit = 25 
    else: 
        plan_name = 'Fiber 50' 
        plan_limit = 50 
        
    return plan_name, plan_limit
    
#INPUT + PROCESS .2 
def data_used_input(plan_limit): #get user's data and compute remaining data 
    while True: 
        try:
            print('Enter data used:') 
            user_input = int(input('-> ')) 
            if user_input > plan_limit: 
                invalid_input() 
                print('Must not exceed Monthly Data Limit.')
            else: 
                remaining_data = plan_limit - user_input 
                return user_input, remaining_data
        except ValueError:
            invalid_input()
    
#OUTPUT 
#display results based from inputs 
def show_result(plan_name, 
    plan_limit, 
    data_used, 
    remaining_data): 
    header() 
    print('D A T A    U S A G E    C H E C K E R') 
    header() 
    time.sleep(0.8) 
    print('Plan: ', plan_name) 
    print('Data Limit: ', plan_limit, ' GB') 
    print('Data Used: ', data_used, ' GB') 
    print('Remaining: ', remaining_data,' GB') 
    if remaining_data > 0:
        print('You are within your data limit.')
    elif remaining_data == 0:
        print('You have reached your data limit.')
    header()

#would you like to try again? 
def return_menu(): 
    print('Check again?') 
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

#MANAGER 
def simulate_checking(): 
    header() 
    internet_plan = internet_plan_name() 
    
    plan_name, plan_limit = classify_internet_plan(internet_plan) 
    
    data_used, remaining_data = data_used_input(plan_limit) 
    show_result(plan_name, 
        plan_limit, 
        data_used, 
        remaining_data)



