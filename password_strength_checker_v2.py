#An updated version of Password Checker v1 checking the strength of a password.

#Utility functions//

#header-
def header():
    print()
    print('————————————————————————————————————')
    print()

#invalid input-
def invalid_input():
    print()
    print('-- Invalid Input! Please Retry.--')
    
#Input function//
def password_input():
    print('Enter Password:')
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
            
#Processing functions//

#Strength analysis-
def check_strength(password):
    
    strength_count = 0
    
    has_upper = False
    has_lower = False
    has_number = False

    for letter in password:
        if letter.isupper():
            has_upper = True
            
        if letter.islower():
            has_lower = True
            
        if letter.isdigit():
            has_number = True
    
    if len(password) >= 8:
        strength_count += 1

    if has_upper:
        strength_count += 1

    if has_lower:
        strength_count += 1

    if has_number:
        strength_count += 1
                
    if strength_count >= 4:
        classification = "Strong"

    elif strength_count >= 2:
        classification = "Medium"

    else:
        classification = "Weak"

    return classification
#Output functions//

#display
def display_strength(password, strength):
    header()
    print('Password:', password)
    print()
    print('Strength Classification:', strength)
    header()    

#check another or exit?
def return_menu():
    print('Would you like to continue?')
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
            
#Manager function
def check_password():
    header()
    print('  A N I M O  P A S S W O R D  C H E C K E R')
    header()
    
    password = password_input()
    
    strength = check_strength(password)
        
    display_strength(password, strength)
    
## -- MAIN PROGRAM -- ##
while True:
    check_password()
    
    if not return_menu():
        break
        
header()
print('Thank you for trusting our service.')
    