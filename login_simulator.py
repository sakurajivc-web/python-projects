#A simple login system.

#Utility functions//

#header-
def header():
    print()
    print('———————————————————————————————————————————')
    print()
    
#incorrect input-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input functions//

#username-
def username_input():
    print('Enter Username:')
    while True:
        get_username = input('-> ').strip()
        if get_username == '':
            invalid_input()
        else:
            return get_username
            
#password-
def password_input():
    print('Enter Password:')
    while True:
        get_password = input('-> ').strip()
        if get_password == '':
            invalid_input()
        else:
            return get_password
            
#Processing functions//

#correct credentials-
username_cc = 'admin'
password_cc = 'Animo123'

#validate input-
def input_validation(username, password):
    if username == username_cc:
        usern_passed = 'Passed'
    else:
        usern_passed = 'Incorrect'
    if password == password_cc:
        passw_passed = 'Passed'
    else:
        passw_passed = 'Incorrect'
        
    return usern_passed, passw_passed
    
#account satatus-
def login_status(usern_passed, passw_passed):
    if usern_passed == 'Passed' and passw_passed == 'Passed':
        access_message = 'Access Granted'
        status_message = 'Successfully Logged In!'
    elif usern_passed == "Passed" and passw_passed == 'Incorrect':
        access_message = 'Access Denied'
        status_message = 'Incorrect Password'
    elif usern_passed == "Incorrect" and passw_passed == 'Passed':
        access_message = 'Access Denied'
        status_message = 'Unkown Username'
    elif usern_passed == "Incorrect" and passw_passed == 'Incorrect':
        access_message = 'Access Denied'
        status_message = 'Incorrect Username and Password!'
    else:
        access_message = 'Access Denied'
        status_message = "Unexpected Error"   
    return status_message, access_message

#Output functions//

#display results-
def login_display(usern_passed, 
    passw_passed, 
    status, 
    access):
    
    header()
    print('      A  N  I  M  O     L  O  G — I  N')
    header()
    print('Username:', usern_passed)
    print('Password:', passw_passed)
    header()
    print(access)
    print(status)
    header()
 
#login again or exit?
def return_menu():
    print('Would you like to retry?')
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
            
#Manager function//
def simulate_login():
    header()
    print('         L O G — I N    S Y S T E M')
    header()
    
    username = username_input()
    password = password_input()
    
    usern_passed, passw_passed = input_validation(username, password)
    status, access = login_status(usern_passed, passw_passed)
        
    login_display(usern_passed, 
    passw_passed, 
    status, 
    access)
     
    return usern_passed, passw_passed
## -- MAIN PROGRAM -- ##
while True:
    usern_passed, passw_passed = simulate_login()
    
    if #A simple login system.

#Utility functions//

#header-
def header():
    print()
    print('———————————————————————————————————————————')
    print()
    
#incorrect input-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input functions//

#username-
def username_input():
    print('Enter Username:')
    while True:
        get_username = input('-> ').strip()
        if get_username == '':
            invalid_input()
        else:
            return get_username
            
#password-
def password_input():
    print('Enter Password:')
    while True:
        get_password = input('-> ').strip()
        if get_password == '':
            invalid_input()
        else:
            return get_password
            
#Processing functions//

#correct credentials-
username_cc = 'admin'
password_cc = 'Animo123'

#validate input-
def input_validation(username, password):
    if username == username_cc:
        usern_passed = 'Passed'
    else:
        usern_passed = 'Incorrect'
    if password == password_cc:
        passw_passed = 'Passed'
    else:
        passw_passed = 'Incorrect'
        
    return usern_passed, passw_passed
    
#account satatus-
def login_status(usern_passed, passw_passed):
    if usern_passed == 'Passed' and passw_passed == 'Passed':
        access_message = 'Access Granted'
        status_message = 'Successfully Logged In!'
    elif usern_passed == "Passed" and passw_passed == 'Incorrect':
        access_message = 'Access Denied'
        status_message = 'Incorrect Password'
    elif usern_passed == "Incorrect" and passw_passed == 'Passed':
        access_message = 'Access Denied'
        status_message = 'Unkown Username'
    elif usern_passed == "Incorrect" and passw_passed == 'Incorrect':
        access_message = 'Access Denied'
        status_message = 'Incorrect Username and Password!'
    else:
        access_message = 'Access Denied'
        status_message = "Unexpected Error"   
    return status_message, access_message

#Output functions//

#display results-
def login_display(usern_passed, 
    passw_passed, 
    status, 
    access):
    
    header()
    print('      A  N  I  M  O     L  O  G — I  N')
    header()
    print('Username:', usern_passed)
    print('Password:', passw_passed)
    header()
    print(access)
    print(status)
    header()
 
#login again or exit?
def return_menu(usern_passed, passw_passed):
    print('Would you like to retry?')
    print('[Y] — Yes')
    print('[N] — No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == '':
            invalid_input()
        elif usern_passed == 'Passed' and passw_passed == 'Passed':
            return True
        elif choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            invalid_input()
            
#Manager function//
def simulate_login():
    header()
    print('         L O G — I N    S Y S T E M')
    header()
    
    username = username_input()
    password = password_input()
    
    usern_passed, passw_passed = input_validation(username, password)
    status, access = login_status(usern_passed, passw_passed)
        
    login_display(usern_passed, 
    passw_passed, 
    status, 
    access)
     
    return usern_passed, passw_passed
## -- MAIN PROGRAM -- ##
while True:
    usern_passed, passw_passed = simulate_login()
    if usern_passed == "Passed" and passw_passed == 'Passed':
        break
    if not return_menu():
        break

header()





