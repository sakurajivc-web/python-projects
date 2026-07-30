#A program that lets the user select movie, giving it a rating.

#Utility functions//

#header-
def header():
    print()
    print('———————————————————————————————————————')
    print()

#if input is invalid-    
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Movie List/
movies = ['Interstellar', 'Spider-Man', 'Top Gun', 'Cars']

#Input Functions//

#choose a movie-
def movie_selection_input():
    print('Select a Movie to rate:')
    print(movies[0], '— 1')
    print(movies[1], '— 2')
    print(movies[2], '— 3')
    print(movies[3], '— 4')
    while True:
        get_movie_selection = int(input('-> '))
        if get_movie_selection < 1 or get_movie_selection > 4:
            invalid_input()
        else:
            selected_movie = movies[get_movie_selection - 1]
            return selected_movie
            
#enter rating for movie-
def movie_rating_input(movie):
    print('What would you rate', movie + '?')
    print('1 — 10')
    while True:
        get_rating = int(input('-> '))
        if get_rating < 1 or get_rating > 10:
            invalid_input()
        else:
            return get_rating
            
#Processing function//
def rating_type(rating):
    if rating <= 2:
        rating_type = 'Bad'
    elif rating <= 4:
        rating_type = 'Average'
    elif rating <= 6:
        rating_type = 'Good'
    elif rating <= 8:
        rating_type = 'Great'
    else:         
        rating_type = 'Masterpiece'
        
    return rating_type
    
#Output functions//

#display results-
def movie_rating_display(movie, 
    rating, 
    classification):
    header()
    print('   A N I M O   M O V I E   R A T I N G')
    header()
    print('Movie Selected:', movie)
    print()
    print('Rating:', rating)
    print()
    print('Classification:', classification)
    header()
    
#rate another movie?-
def return_menu():
    print('Rate another Movie?')
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
def rate_movie():
    header()
    print('    A N I M O   M O V I E   R A T E R')
    header()
    movie = movie_selection_input()
    print()
    rating = movie_rating_input(movie)
    
    classification = rating_type(rating)
    header()
    
    movie_rating_display(movie, 
    rating,
    classification)
    
## -- MAIN PROGRAM -- ##
while True:
    rate_movie()
    
    if not return_menu():
        break
print('Thank you for using our rating app. You got neat taste!')
header()