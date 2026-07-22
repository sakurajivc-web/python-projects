#A program that simulates an ISP Wi-Fi installation service to users.

#function for header//
def header():
    print()
    print('——————————————————————————————————————————————————————————') 
    print()
    
#function for invalid inputs//
def invalid_input():
    print()
    print('--Invalid Input! Please retry.--')
    
#Input Functions//

#name-
def name_input():
    print('Enter Name:')
    while True:
        get_name = input('-> ').strip().title()
        if get_name == '':
            invalid_input()
        else:
            return get_name
            
#address-
def address_input():
    print('Enter Installation Address:')
    while True:
        get_address = input('-> ').strip().upper()
        if get_address == '':
            invalid_input()
        else:
            return get_address
            
#installation type choice-
def installation_choice_input():
    print('Enter Installation Type:')
    print('[1] - New Installation')
    print('[2] - Renewal / Upgrade')
    while True:
        try:
            get_type = int(input('-> '))
            if get_type < 1 or get_type > 2:
                invalid_input()
            else:
                return get_type
        except ValueError:
            invalid_input()
            continue

#speed choice-
def speed_choice_input():
    print('Enter Speed Plan:')
    print('[1] - 100 MBPS - 500 PHP p/m')
    print('[2] - 250 MBPS - 1099 PHP p/m')
    print('[3] - 500 MBPS - 2299 PHP p/m')
    while True:
        try:
            get_speed_plan = int(input('-> '))
            if get_speed_plan < 1 or get_speed_plan > 3:
                invalid_input()
            else:
                return get_speed_plan
        except ValueError:
            invalid_input()
            continue
            
#Processing Functions//

#Plan Details-
def plan_details(installation_type, speed_choice):
    if installation_type == 1:
        installation_fee_price = 1000
        type = 'New Installation'
    else:
        installation_fee_price = 0
        type = 'Renewal / Upgrade'
       
    if speed_choice == 1:
        name = 'Basic'
        speed = '100 MBPS'
        price = 500
    elif speed_choice == 2:
        name = 'Regular'
        speed = '250 MBPS'
        price = 1099 
    else:
        name = 'Premium'
        speed = '500 MBPS'
        price = 2299
        
    return installation_fee_price, type, name, speed, price

#total amount due-
def compute_total(monthly_fee, installation_fee):
    computed_total =  monthly_fee + installation_fee
        
    return computed_total
        
#Output function//
def booking_summary(customer_name, 
address, 
install_type, 
plan_name, 
internet_speed, 
monthly_fee, 
installation_fee, 
total_price):
    header()
    print('   A N I M O    W I — F I    INSTALLATION')
    header()
    print('Customer:', customer_name)
    print('Installation Address:', address)
    header()
    print('Installation Type:', install_type)
    print('Selected Plan:', plan_name)
    print('Internet Speed:', internet_speed)
    header()
    print('Plan Monthly Fee:', monthly_fee, 'PHP')
    print('Installation Fee:', installation_fee, 'PHP')
    header()
    print('Total Amount Due:', total_price, 'PHP')
    header()
    

#install again or exit?-
def return_menu():
    print('Install new plan?')
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
            
#manager function//
def wifi_booking():
    header()
    customer_name = name_input()
    print()
    address = address_input()
    print()
    installation_type = installation_choice_input()
    print()
    speed_choice = speed_choice_input()
    
    installation_fee, install_type, plan_name, internet_speed, monthly_fee = plan_details(installation_type, speed_choice)
    total_price = compute_total(monthly_fee, installation_fee)
    
    booking_summary(customer_name, 
        address, 
        install_type, 
        plan_name, 
        internet_speed, 
        monthly_fee, 
        installation_fee, 
        total_price)

## -- MAIN PROGRAM -- ##
while True:
    wifi_booking()
    
    if not return_menu():
        break
        
header()
print('Thank you for using ANIMO HOME FIBER WI-FI!')
header()

