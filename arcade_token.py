#Program simulating a user buying arcade tokens.

#Utility Functions//

#header-
def header():
    print()
    print('———————————————————————————————————————————————————')
    print()
    
#if input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
#Starting List
token_package = [
    '20 Tokens', '50 Tokens', '100 Tokens'
]

prices = [
    100, 230, 450
]

#Input Functions .1//

#Token package selection
def token_package_input():
    print('Select a Token Package:')
    print('[1] —', token_package[0], '— ₱', prices[0])
    print('[2] —', token_package[1], '— ₱', prices[1])
    print('[3] —', token_package[2], '— ₱', prices[2])
    print('———————————————————————————————————————————————————')
    while True:
        try:
            get_package = int(input('-> '))
            if get_package < 1 or get_package > 3:
                invalid_input()
            else:
                return get_package
        except ValueError:
            invalid_input()
            
#How many packages?
def package_amount_input():
    print('Enter Amount of Package:')
    print('[1 — 100]')
    print('———————————————————————————————————————————————————')
    while True:
        try:
            get_amount = int(input('-> '))
            if get_amount < 1 or get_amount > 100:
                invalid_input()
            else:
                return get_amount
        except ValueError:
            invalid_input()
            
#Processing Functions .1//

#Determine package and price
def determine_package_number(package_number):
    if package_number == 1:
        package_value = token_package[0]
        package_price = prices[0]
    elif package_number == 2:
        package_value = token_package[1]
        package_price = prices[1]
    else:
        package_value = token_package[2]
        package_price = prices[2]

    return package_value, package_price
    
#Calculate total price
def calculate_total(price, package_amount):
    total_price = price * package_amount
    return total_price
    
#Input and Processing Function .2//

#Payment and Processing
def payment_input_processing(package, package_amount, total):
    print('Selected Package:', package)
    print('Package Amount:', package_amount)
    print()
    print('Please pay the following amount:')
    print('₱', total)
    print('———————————————————————————————————————————————————')
    while True:
        try:
            get_payment = int(input('-> '))
            if get_payment < total:
                invalid_input()
                print()
                print('Insufficient Cash.')
            elif get_payment >= total:
                change = get_payment - total
                return get_payment, change
        except ValueError:
            invalid_input()

#Output Functions//

#Display order receipt
def display_receipt(package, 
    package_amount, 
    price, 
    total, 
    paid, 
    change):
    header()
    print('      A N I M O    T O K E N    R E C E I P T')
    header()
    print('Token Package:', package)
    print('Base Price: ₱', price)
    print('Package Amount:', package_amount)
    print('———————————————————————————————————————————————————')
    print('Total Price: ₱', total)
    print('Amount Paid: ₱', paid)
    print('PChange ₱:', change)
    header()
    
#Order again or exit?
def return_menu():
    print('Would you like to order again?')
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
def simulate_order():
    header()
    print('       A N I M O    T O K E N    B O O T H')
    header()
    
    package_number = token_package_input()
    print()
    package_amount = package_amount_input()
    header()

    package, price = determine_package_number(package_number)
    total = calculate_total(price, package_amount)
    
    paid, change = payment_input_processing(package, package_amount, total)
    
    display_receipt(package, 
    package_amount, 
    price, 
    total, 
    paid, 
    change)
    
## -- MAIN PROGRAM -- ##
while True:
    simulate_order()
    
    if not return_menu():
        break
        
print('Thank you for your purchase!')
header()