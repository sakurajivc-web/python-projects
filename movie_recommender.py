#The user chooses a movie genre, and the program recommends a movie from that genre.

#Utility Functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————————')
    print()
    
#if inout is incorrect-
def invalid_input():
    print()
    print('——Invalid Input! Pleasen retry.———')
        
#lists
genres = ['Action', 'Horror', 'Animation', 'Sci-Fi']
movies = ['Spider-Man: Brand New Day',
'Silent Hill', 
'Toy Story 5',
'Interstellar']

#Input function//

#choose genre
def genre_input():
    print('Select a genre:')
    print('1 —', genres[0])
    print('2 —', genres[1])
    print('3 —', genres[2])
    print('4 —', genres[3])
    while True:
        try:
            get_genre = int(input('-> '))
            if get_genre < 1 or get_genre > 4:
                invalid_input()
            else:
                genre_number = get_genre - 1
                return genre_number
        except ValueError:
            invalid_input()

#Processing function//

#which movie?-
def movie_generator(genre_number):
    movies[genre_number]
    return movies[genre_number]
    
#Output functions//

#display results:
def display_recommendation(genre_number, generated_movie):
    header()
    print('    M O V I E    R E C O M M E N D A T I O N')
    header()
    print('Genre:', genres[genre_number])
    header()
    print('Recommendation:', generated_movie)
    header()

#try again?
def return_menu():
    print('Get another recommendation?')
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
def recommend_movie():
    header()
    
    genre_number = genre_input()
    
    generated_movie = movie_generator(genre_number)
    
    display_recommendation(genre_number, generated_movie)
    
## -- MAIN PROGRAM -- ##
while True:
    recommend_movie()
    
    if not return_menu():
        break
        
print('Hope you liked our recommendation!')
header()







            
