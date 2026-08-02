#A program simulating a snack booth for cinemas where the user can buy a selected snack (and add-on drinks) then paying for it.

#Utility Functions//

#header-
def header():
    print()
    print('———————————————————————————————————————————————')
    print()
    
#if user input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please retry!——')
        
#menu list/
snacks = ['Popcorn', 'Nachos', 'Hotdog']
snacks_prices = [150, 120, 90]
drink_addons = ['Soda', 'Iced Tea', 'Water']
drink_addons_prices = [60, 70, 30]

#Input Functions .1//

#choose a snack-
def snacks_input():
    print('Select your snack:')
    print('1 —', snacks[0], snacks_prices[0], 'PHP')
    print('2 —', snacks[1], snacks_prices[1], 'PHP')
    print('3 —', snacks[2], snacks_prices[2], 'PHP')
    print()
    while True:
        try:
            get_snack = int(input('-> '))
            if get_snack < 1 or get_snack > 3:
                invalid_input()
            else:
                return get_snack
        except ValueError:
            invalid_input()
            
#addon drink?-
def addons_choice():
    print('Would you like to add Drinks?')
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

#choose an addon drink-
def drinks_input():
    want_drink = addons_choice()
    if want_drink:
        header()
        print('Select your drink:')
        print('1 —', drink_addons[0], drink_addons_prices[0], 'PHP')
        print('2 —', drink_addons[1], drink_addons_prices[1], 'PHP')
        print('3 —', drink_addons[2], drink_addons_prices[2], 'PHP')
        while True:
            try:
                get_drinks = int(input('-> '))
                if get_drinks < 1 or get_drinks > 3:
                    invalid_input()
                else:
                    return get_drinks
            except ValueError:
                invalid_input()            
    else:
        get_drinks = 'None'
        return get_drinks

#Processing Functions .1//

#determine selected snack-
def which_snack(snack_choice):
    if snack_choice == 1:
        return snacks[0], snacks_prices[0]
    elif snack_choice == 2:
        return snacks[1], snacks_prices[1]
    elif snack_choice == 3:
        return snacks[2], snacks_prices[2]
    else:
        print("Unexpected snack_choice:", snack_choice)
        return 'No Snacks', 0  
#determine selected drink-
def which_drink(drink_choice):
    if drink_choice == 1:
        return drink_addons[0], drink_addons_prices[0]
    elif drink_choice == 2:
        return drink_addons[1], drink_addons_prices[1]
    elif drink_choice == 3:
        return drink_addons[2], drink_addons_prices[2]
    else:
        print("Unexpected drink_choice:", drink_choice)
        return 'No Addons', 0
#determine total price-
def total_price_calculation(snack_price, drink_price):
    total_price = snack_price + drink_price
    return total_price   
#Input function .2//

#payment-
def order_payment(selected_snack, selected_drinks, total):
    print('Snack:', selected_snack)
    print('Drinks:', selected_drinks)
    print('Please pay the following amount:', total, 'PHP')
    print()
    while True:
        try:
            get_payment = int(input('-> '))
            if get_payment < total:
                invalid_input()
                print()
                print('Insufficient Cash!')
            elif get_payment >= total:
                change = get_payment - total
                return get_payment, change
        except ValueError:
            invalid_input()

#Output Functions//

#display receipt-
def display_order(selected_snack, 
    selected_drinks, 
    snack_price, 
    drink_price, 
    total, 
    paid, 
    change, 
    drink_choice):
    header()
    print('      O  R  D  E  R     R  E  C  E  I  P  T')
    header()
    print('Snack:', selected_snack, '—', snack_price, 'PHP')
    print('Drinks:', selected_drinks, '—', drink_price, 'PHP')
    print()
    print('Total:', total, 'PHP')
    header()
    print('Paid:', paid, 'PHP')
    print('Change:', change, 'PHP')
    header()

#order again?-
def return_menu():
    print('Would you like to add Drinks?')
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
def cinema_snack_booth():
    header()
    print('   A N I M O   C I N E M A   S N A C K   B O O T H')
    header()
    snack_choice = snacks_input()
    print()
    drink_choice = drinks_input()
    
    selected_snack, snack_price = which_snack(snack_choice)
    selected_drinks, drink_price = which_drink(drink_choice)

    total = total_price_calculation(snack_price, drink_price)
    
    paid, change = order_payment(selected_snack, selected_drinks, total)

    display_order(selected_snack, 
    selected_drinks, 
    snack_price, 
    drink_price, 
    total, 
    paid, 
    change, 
    drink_choice)

## -- MAIN PROGRAM -- ##
while True:
    cinema_snack_booth()
    
    if not return_menu():
        break
        
print('Thank you for ordering at Animo Cneima Snacks Booth!')
header()






























































