#User chooses a game to buy, and the program calculates the final price based on their membership.

#Utility funcitons//

#header-
def header():
    print()
    print('——————————————————————————————————————————————')
    print()
    
#invalid input-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Starting Data
games = [
    "Minecraft",
    "Spider-Man 2",
    "EA FC 27",
    "Valorant Points"
]

prices = [
    1500,
    3200,
    2800,
    1000
]

#Input Functions .1//

#choose a game to buy-
def choose_game_input():
    print('Select a game to purchase:')
    print(games[0], '— 1', prices[0], 'PHP')
    print(games[1], '— 2', prices[1], 'PHP')
    print(games[2], '— 3', prices[2], 'PHP')
    print(games[3], '— 4', prices[3], 'PHP')
    print('——————————————————————————————————————————————')
    while True:
        try:
            get_selection = int(input('-> '))
            if get_selection < 1 or get_selection > 4:
                invalid_input()
            else:
                return get_selection
        except ValueError:
            invalid_input()
            
#is user a store member?-
def ask_user():
    print('Are you a member of the store?')
    print('[Y] — Yes')
    print('[N] — No')
    print('——————————————————————————————————————————————')
    while True:
        answer = input('-> ').strip().upper()
        if answer == '':
            invalid_input()
        elif answer == 'Y' or answer == 'YES':
            return True
        elif answer == 'N' or answer == 'NO':
            return False
        else:
            invalid_input()
            
#Processing Functions//

#determine discount for user-
def determine_discount(member):
    if member:
        discount_percentage = '10%'
        discount_value = 0.9
    else:
        discount_percentage = 'None'
        discount_value = 1
        
    return discount_percentage, discount_value

#determine price and movie-
def determine_price_and_movie(selected):
    if selected == 1:
        which_game = games[0] 
        game_price = prices[0]
    elif selected == 2:
        which_game = games[1] 
        game_price = prices[1]
    elif selected == 3:
        which_game = games[2] 
        game_price = prices[2]
    else:
        which_game = games[3] 
        game_price = prices[3]
    
    return which_game, game_price
    

#calculate price-
def calculate_total(price, dscnt_value):
    total_calculated_price = price * dscnt_value
    return total_calculated_price
    
#Input and Process functions .2//

#Payment
def counter_payment(game, total_price, discount_percent):
    print('Selected Game:', game)
    print('Discount:', discount_percent)
    print('Amount to Pay:', total_price, 'PHP')
    print('——————————————————————————————————————————————')
    while True:
        try:
            get_payment = int(input('-> '))
            if get_payment < total_price:
                invalid_input()
                print()
                print('Insufficient Cash.')
            elif get_payment >= total_price:
                payment_change = get_payment - total_price
                return get_payment, payment_change
        except ValueError:
            invalid_input()
            

#Output functions//

#purchase receipt-
def display_receipt(game, 
    price, 
    discount_percent, 
    total_price, 
    paid, 
    change):
    header()
    print('     G A M E    S H O P    R E C E I P T')
    header()
    print('Game:', game)
    print('Price:', price, 'PHP')
    print()
    print('Discount:', discount_percent)
    print('Final Price:', total_price, 'PHP')
    print()
    print('Paid:', paid, 'PHP')
    print('Change', change, 'PHP')
    header()
    
#buy another?- 
def return_menu():
    print('Would you like to order again?')
    print('[Y] — Yes')
    print('[N] — No')
    print('——————————————————————————————————————————————')
    while True:
        answer = input('-> ').strip().upper()
        if answer == '':
            invalid_input()
        elif answer == 'Y' or answer == 'YES':
            return True
        elif answer == 'N' or answer == 'NO':
            return False
        else:
            invalid_input()

#Manager Function//
def simulate_shop():
    header()
    print('   A  N  I  M  O     G  A  M  E     S  H  O  P')
    header()
    selected = choose_game_input()
    print()
    member = ask_user()

    discount_percent, dscnt_value = determine_discount(member)
    
    game, price = determine_price_and_movie(selected)

    total_price = calculate_total(game, price, dscnt_value)

    header()
    paid, change = counter_payment(game, total_price, discount_percent)

    display_receipt(game, 
    price, 
    discount_percent, 
    total_price, 
    paid, 
    change)           

## -- MAIN PROGRAM -- ##
while True:
    simulate_shop()
    
    if not return_menu():
        break
        
print('Thank you for ordering!')
header()