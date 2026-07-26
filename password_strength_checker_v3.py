#A realistic password validator that evaluates password strength based on multiple factors-providing detailed feedback.

#Utility functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————————')
    print()

#if input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input function//

#password-
def password_input():
    print('Enter Password:')
    while True:
        get_password = input('-> ').strip()
        if get_password == '':
            invalid_input()
        elif len(get_password) < 4:
            invalid_input()
            print()
            print('Please enter 4 or more characters.')
        elif len(get_password) <= 50:
            return get_password
        else:
            invalid_input()
            print()
            print('Password exceeds maximum characters.')
            
#Processing function//
def strength_checker(password):
    
    strength_count = 0
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_spc = False
    
    
    for characters in password:
        if characters.isupper():
            has_upper = True
            
        if characters.islower():
            has_lower = True
            
        if characters.isdigit():
            has_digit = True 
            
        if not characters.isalnum():
            has_spc = True
    
    if len(password) >= 8:
        length_passed = 'Passed'
    else:
        length_passed = 'Failed'
        
    if has_upper:
        upper_passed = 'Passed'
    else:
        upper_passed = 'Failed'
        
    if has_lower:
        lower_passed = 'Passed'
    else:
        lower_passed = 'Failed'
  
    if has_digit:
        digit_passed = 'Passed'
    else:
        digit_passed = 'Failed'
           
    if has_spc:
        spc_passed = 'Passed'
            
    else:
        spc_passed = 'Failed' 
    
    if len(password) >= 8:
        strength_count += 1
        
    if has_upper:
        strength_count += 1
        
    if has_lower:
        strength_count += 1

    if has_digit:
        strength_count += 1 
    
    if has_spc:
        strength_count += 1
        
    if strength_count <= 1:
        classification = 'Very Weak'
        
    elif strength_count <= 2:
        classification = 'Weak'
        
    elif strength_count <= 3:
        classification = 'Medium'
        
    elif strength_count <= 4:
        classification = 'Strong'
    
    else:
        classification = 'Very Strong'
        
    return (length_passed, 
        upper_passed, 
        lower_passed, 
        digit_passed, 
        spc_passed, 
        classification)
        
#Output functions//

#Detailed results-
def detailed_results(password, 
    length, 
    upperc, 
    lowerc, 
    number, 
    special_c, 
    strength):
    
    header()
    print('       R   E   S   U   L   T   S')
    header()
    print('Password:', password)
    print()
    print('Length:', length)
    print('Uppercase:', upperc)
    print('Lowercase:', lowerc)
    print('Number:', number)
    print('Special Character:', special_c)
    header()
    print('Password Strength:', strength)
    header()

#Check another or exit?-    
def return_menu():
    print('Would you like to check another password?')
    print('[Y] — Yes')
    print('[N] — No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == '':
            invalid_input()
        elif choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            invalid_input()
            continue
            
#Manager function//
def check_password():
    header()
    print('   A N I M O   P A S S W O R D   C H E C K E R')
    header()
    password = password_input()
    
    length, upperc, lowerc, number, special_c, strength = strength_checker(password)
    
    detailed_results(password, 
    length, 
    upperc, 
    lowerc, 
    number, 
    special_c, 
    strength)
    
## -- MAIN PROGRAM -- ##
while True:
    check_password()
    
    if not return_menu():
        break
header()        
print('Thank you for using Animo Password Checker!')
header()