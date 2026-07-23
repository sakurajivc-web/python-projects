#A program that checks the strength of the user's given password.

#Utility functions//

def header():
    print()
    print('——————————————————————————————————————————')
    print()
    
def invalid_input():
    print()
    print('--Invalid Input! Please Retry.--')
    
#Input function//
#password
def password_input():
    print('Enter Password to check:')
    while True:
        get_password = input('-> ').strip()
        if get_password == '':
            invalid_input()
        elif len(get_password) < 4:
            invalid_input()
            print('Enter 4 or more characters!')
        elif len(get_password) <= 50:
            return get_password
        else:
            invalid_input()
            print('Password must not exceed 50 characters!')
            
#Processing function//
#strength classification
def check_strength(password):
    if len(password) < 8:
        strength_class = 'Weak'
    elif len(password) < 15:
        strength_class = 'Medium'
    else:
        strength_class = 'Strong'
    
    return strength_class
    
#Output functions//
#display result
def display_password_strength(password, strength):
    header()
    print('Password:', password)
    print()
    print('Password Strength:', strength)
    header()
    
#check another password or exit?
def return_menu():
    print('Check another password?')
    print('[Y] - Yes')
    print('[N] - No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            invalid_input()
            
#Manager for main program
def password_strength_checker():
    header()
    print('  A N I M O  P A S S W O R D  C H E C K E R')
    header()
    password = password_input()
    
    strength = check_strength(password)
    display_password_strength(password, strength)
    
## -- MAIN PROGRAM -- ##
while True:
    password_strength_checker()
    
    if not return_menu():
        break
        
header()
print('Thank you for using Animo Password Checker!')



