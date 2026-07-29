#A program that simulates an organization tool or a movie list.

#Utility Functions

#Header-
def header():
    print()
    print('———————————————————————————————————————————————————————————————————')
    print()
    
#Invalid Inputs-
def invalid_input():
    print()
    print('——Invalid Input! Please retry.——')

#Movie Collections
movies = ['Spiderman BND', 'Avengers Doomsday', 'Michael Pt.1', 'Silent Hill']

#Input functions//

#which movie to replace-
def choose_movie_input(movies):
    print('Select Movie to Replace:')
    print(movies[0], '— 1')
    print(movies[1], '— 2')
    print(movies[2], '— 3')
    print(movies[3], '— 4')
    while True:
        get_movie = int(input('-> '))
        if get_movie < 1 or get_movie > 4:
            invalid_input()
        else:
            return get_movie
            
#new movie title-  
def new_movie_name_input():
    print('Enter New Movie Name:')
    while True:
        get_new_name = input('-> ').strip().title()
        if get_new_name == '':
            invalid_input()
        else:
            return get_new_name 
         
#Processing Functions//
def replace_movie(movie_number, new_movie_name):
    
    old_movie = movies[movie_number - 1]
    
    movies[movie_number - 1] = new_movie_name
    
    return old_movie
    
#Output Functions//

#Display updated list and changes-
def display_movie_list(old_movie_name, new_movie_name):
    header()
    print('  A  N  I  M  O     M  O  V  I  E     O  R  G  A  N  I  Z  E  R ')
    header()
    print('Movie Updated Successfully!')
    print()
    print('Movie List')
    print(movies)
    header()
    print('Old Movie:')
    print(old_movie_name)
    print()
    print('New Movie:')
    print(new_movie_name)
    header()

#replace another movie or exit?
def return_menu():
    print('Would you like to replace another movie?')
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
def replace_a_movie():
    header()
    movie_number = choose_movie_input(movies)
    print()
    new_movie_name = new_movie_name_input()
    
    old_movie_name = replace_movie(movie_number, new_movie_name)

    display_movie_list(old_movie_name, new_movie_name)

## -- MAIN PROGRAM -- ##
while True:
    replace_a_movie()
    
    if not return_menu():
        break
        
print('Nice movie taste you got there! Thanks for using our movie organizer!')
header()
