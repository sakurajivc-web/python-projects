#A program simulating a coffee shop where customer orders one coffee, chooses a cup size, and the program computes the total price.

#Utility Functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————————')
    print()
    
#invalid input-
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')
        
#Starting Data
coffee = [
    "Americano",
    "Latte",
    "Mocha",
    "Espresso"
]

prices = [
    120,
    150,
    170,
    100
]

cup_sizes_and_price = [
    "(1) Small  — +0  PHP",
    "(2) Medium — +20 PHP",
    "(3) Large  — +40 PHP"
]

#Input Functions .1//

#Choose Coffee
def coffee_input():
    print('Select Coffee:')
    print('(1)', coffee[0])
    print('(2)', coffee[1])
    print('(3)', coffee[2])
    print('(4)', coffee[3])
    print('——————————————————————————————————————————————')
    while True:
        try:
            get_coffee = int(input('-> '))
            if get_coffee < 1 or get_coffee > 4:
                invalid_input()
            else:
                return get_coffee
        except ValueError:
            invalid_input()

#Choose Cup Size
def cup_size_input():
    print('Select Cup Size:')
    print('(1)', cup_sizes_and_price[0])
    print('(2)', cup_sizes_and_price[1])
    print('(3)', cup_sizes_and_price[2])
    print('——————————————————————————————————————————————')
    while True:
        try:
            get_cup_size = int(input('-> '))
            if get_cup_size < 1 or get_cup_size > 3:
                invalid_input()
            else:
                return get_cup_size
        except ValueError:
            invalid_input()

#Processing Functions .1//

#Which Coffee, Base Price, Size, and Size Price
def determine_order(selected_coffee, selected_cup_size):
    if selected_coffee == 1:
        which_coffee = coffee[0]
        coffee_base_price = prices[0]
    elif selected_coffee == 2:
        which_coffee = coffee[1]
        coffee_base_price = prices[1]
    elif selected_coffee == 3:
        which_coffee = coffee[2]
        coffee_base_price = prices[2]
    else:
        which_coffee = coffee[3]
        coffee_base_price = prices[3]
    
    if selected_cup_size == 1:
        which_cup_size = 'Small'
        add_size_price = 0
    elif selected_cup_size == 2:
        which_cup_size = 'Medium'
        add_size_price = 20
    else:
        which_cup_size = 'Large'
        add_size_price = 40
        
    return which_coffee, coffee_base_price, which_cup_size, add_size_price


#Total Price Calculation
def determine_total_price(base_price, size_price):
    coffee_total_price = base_price + size_price
    return coffee_total_price
    
#Input and Processing Function .2//

#Payment and Processing
def payment_input(coffee, size, total_price):
    print('Order:', coffee, '—', size)
    print('Please pay the following amount:')
    print(total_price, 'PHP')
    print('——————————————————————————————————————————————')
    while True:
        try:
            get_payment = int(input('-> '))
            if get_payment < total_price:
                invalid_input()
                print()
                print('Insufficient Cash.')
            elif get_payment >= total_price:
                get_change = get_payment - total_price
                return get_payment, get_change
        except ValueError:
            invalid_input()

#Output Functions//

#Display Order
def receipt_display(coffee, 
    size, 
    base_price, 
    size_price, 
    total_price, 
    paid, 
    change
):
    header()
    print('     A N I M O    C O F F E E    R E C E I P T')
    header()
    print('Coffee Ordered:', coffee)
    print('Order Size:', size)
    header()
    print('Coffee Price:', base_price, 'PHP')
    print('Size Price:', size_price, 'PHP')
    print()
    print('Total:', total_price, 'PHP')
    header()
    print('Cash Paid:', paid, 'PHP')
    print('Payment Change:', change, 'PHP')
    header()

#Order again?
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
def take_order():
    header()
    print('      A N I M O    C O F F E E    S H O P')
    header()
    
    selected_coffee = coffee_input()
    print()
    selected_cup_size = cup_size_input()
    header()
    
    coffee, base_price, size, size_price = determine_order(selected_coffee, selected_cup_size)
    total_price = determine_total_price(base_price, size_price)
    
    paid, change = payment_input(coffee, size, total_price)
    
    receipt_display(coffee, 
    size, 
    base_price, 
    size_price, 
    total_price, 
    paid, 
    change)

## -- MAIN PROGRAM -- ##
while True:
    take_order()
    
    if not return_menu():
        break
        
print('Thank you for ordering at Animo Coffee!')
header()
