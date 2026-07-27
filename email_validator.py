#A program that checks whether an email is valid with basic rules.

#Utility functions//

#header-
def header():
    print()
    print('————————————————————————————————————————————————')
    print()

#invalid input-    
def invalid_input():
    print()
    print('——Please retry! Invalid Input.——')


#Input function//
def email_input():
    print('Enter Email:')
    while True:
        get_email = input('-> ').strip()
        if get_email == '':
            invalid_input()
        else:
            return get_email
            
#Processing function//
def validate_email(email):
    
    if len(email) < 9:
        length_check = 'Failed'
    else:
        length_check = 'Passed'
        
    if not email.count('@'):
        at_check = 'Failed'
    else:
        at_check = 'Passed'
        
    if not email.count('.'):
        dot_check = 'Failed'
    else:
        dot_check = 'Passed'
        
    if email.count(' '):
        space_check = 'Failed'
    else:
        space_check = 'Passed'
     
    return (length_check, 
        at_check, 
        dot_check, 
        space_check)
    
def email_validity(checked_length, 
    checked_at, 
    checked_dot, 
    checked_space):
    
    if (
    checked_length == "Passed"
    and checked_at == "Passed"
    and checked_dot == "Passed"
    and checked_space == "Passed"
    ):
        validity = "Valid"
    else:
        validity = "Invalid"
    
    return validity
#Output funtions//

#display checked email 
def display_result(email, 
    checked_length, 
    checked_at, 
    checked_dot, 
    checked_space,
    validity):
    header()
    print('     R   E   S   U   L   T   S')
    header()
    print('Email:', email)
    header()
    print('Length:', checked_length)
    print('Contains @:', checked_at)
    print('Contains .:', checked_dot)
    print('Contains Spaces:', checked_space)
    header()
    print('Email Status:')
    print(validity)
    header()

#check another or exit?
def return_menu():
    print('Check another email?')
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

#Manager Function//
def check_email():
    header()
    print('    A N I M O   E M A I L   V A L I D A T O R')
    header()
    
    email = email_input()
    
    checked_length, checked_at, checked_dot, checked_space = validate_email(email)
    validity = email_validity(checked_length, checked_at, checked_dot, checked_space)
    
    display_result(email, 
    checked_length, 
    checked_at, 
    checked_dot, 
    checked_space,
    validity)
        
## -- MAIN PROGRAM -- ##
while True:
    check_email()
    
    if not return_menu():
        break
        
print('Thank you for using Animo Email Evaluator!')
header()
    





















    