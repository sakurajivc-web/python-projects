#A program that lets the user select a ovie and enter their age, dtermening the ticker price for the user to pay, then displaying the results.

#Utility Functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————')
    print()
    
#if the input is invalid-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')


#list of available movies:
movies = ['Spiderman', 'Toys', 'Backrooms', 'The Silence']
movie_prices = [400, 200, 300, 350]  
        
#Input functions .1//

#select a movie to watch-
def selected_movie_input():
    print('Choose a Movie:')
    print('1 —', movies[0], movie_prices[0], 'PHP')
    print('2 —', movies[1], movie_prices[1], 'PHP')
    print('3 —', movies[2], movie_prices[2], 'PHP')
    print('4 —', movies[3], movie_prices[3], 'PHP')
    while True:
        get_movie_choice = int(input('-> '))
        if get_movie_choice < 1 or get_movie_choice > 4:
            invalid_input()
        else:
            return get_movie_choice
            
#select user age-
def user_age_input():
    print('Enter Age:')
    while True:
        get_age = int(input('-> '))
        if get_age < 1 or get_age > 125:
            invalid_input()
        else:
            return get_age
            
#Processing Functions//

#detrmine selected movie-
def which_movie(selected_movie):
    if selected_movie == 1:
        return movies[0]
    elif selected_movie == 2:
        return movies[1]
    elif selected_movie == 3:
        return movies[2] 
    else:
        return movies[3]

#determine price of movie-
def movie_ticket_price(selected_movie):
    if selected_movie == 1:
        return movie_prices[0]
    elif selected_movie == 2:
        return movie_prices[1]
    elif selected_movie == 3:
        return movie_prices[2] 
    else:
        return movie_prices[3]
          
#determine final price of ticket based on user's age-
def final_ticket_price(movie_price, age):
    if age <= 12:
        final_ticket_price = movie_price * 0.75
    elif age <= 17:
        final_ticket_price = movie_price * 0.85
    elif age <= 59:
        final_ticket_price = movie_price * 1
    else:
        final_ticket_price = movie_price * 0.95
    
    return final_ticket_price
    
#Input function .2//

#Payment for ticket-
def ticket_payment(movie, ticket_price):
    print('Selected Movie Ticket:', movie)
    print('Please pay the following amount:')
    print('Ticket Price:', ticket_price, 'PHP')
    while True:
        get_payment = int(input('-> '))
        if get_payment > ticket_price:
            change = get_payment - ticket_price
            return change, get_payment 
        elif get_payment == ticket_price:
            change = get_payment - ticket_price
            return change, get_payment 
        elif get_payment < ticket_price:
            invalid_input()
            print()
            print('Insuffiecient Cash. Pay exact amount.')
        else:
            print('Unexpected Error!')
            
#Output functions//

#purchase receipt-
def purchase_receipt(movie, 
    age, 
    ticket_price, 
    change, 
    paid):
    header()
    print('    A  N  I  M  O     C  I  N  E  M  A  S')
    header()
    print('Movie:', movie)
    print('Customer Age:', age)
    print()
    print('Ticket Price:', ticket_price, 'PHP')
    header()
    print('Paid:', paid, 'PHP')
    print('Change:', change, 'PHP')
    header()

#serve another customer?
def return_menu():
    print('Would you like to purchase another ticket?')
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
def ticket_booth():
    header()
    print('    A  N  I  M  O     C  I  N  E  M  A  S')
    header()
    
    selected_movie = selected_movie_input()
    print()
    age = user_age_input()
    
    movie = which_movie(selected_movie)
    movie_price = movie_ticket_price(selected_movie)
    
    ticket_price = final_ticket_price(movie_price, age)

    header()
    change, paid = ticket_payment(movie, ticket_price)

    purchase_receipt(movie, 
    age, 
    ticket_price, 
    change, 
    paid)

## -- MAIN PROGRAM -- ##
while True:
    ticket_booth()
    
    if not return_menu():
        break

print('Thank you for visiting Animo Ticket Booth!')
header()