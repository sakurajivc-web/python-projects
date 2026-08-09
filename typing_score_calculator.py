#A program that calculates the user's WPM based from words typed and minutes spent typing.

#Utility Functions//

#Header
def header():
    print()
    print('———————————————————————————————————————————————')
    print()
    
#Invalid Input
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
    
#Input Functions//

#Username
def username_input():
    print('Enter Username:')
    print('———————————————————————————————————————————————')
    while True:
        get_username = input('-> ').strip()
        if get_username == '':
            invalid_input()
        else:
            return get_username
            
#Words Typed
def words_typed_input():
    print('Enter Words Typed: [Amount]')
    print('———————————————————————————————————————————————')
    while True:
        try:
            get_words_typed = int(input('-> '))
            if get_words_typed < 1:
                invalid_input()
            else:
                return get_words_typed
        except ValueError:
            invalid_input()
            
#Time spent typing
def time_minutes_input():
    print('Enter Time Spent Typing: [Minutes: 1 —100]')
    print('———————————————————————————————————————————————')
    while True:
        try:
            get_time_minutes = int(input('-> '))
            if get_time_minutes < 1 or get_time_minutes > 100:
                invalid_input()
            else:
                return get_time_minutes
        except ValueError:
            invalid_input()
            
#Processing Function//

#Determine User WPM 
def calculate_wpm(words_typed, time_minutes):
    calculated_wpm = words_typed / time_minutes
    return round(calculated_wpm, 2)

#Rate WPM
def check_rating(wpm):
    if wpm < 20:
        return 'Very Slow...'
    elif wpm < 40:
        return 'Slow..'
    elif wpm < 50:
        return 'Average'
    elif wpm < 60:
        return 'Above Average!'
    elif wpm < 75:
        return 'Fast!'
    else:
        return 'Excellent!!'
            
#Output Functions//

#Show typing results
def display_results(username, 
    words_typed, 
    time_minutes, 
    wpm, 
    rating):
    
    header()
    print('     T Y P I N G    S C O R E')
    header()
    print(username + "' score:")
    print()
    print('Words Typed:', words_typed)
    print('Minutes:', time_minutes)
    print()
    print('WPM:', wpm)
    print('Rating:', rating)
    header()
    
#Try again?
def return_menu():
    print('Would you like to check again?')
    print('[Y] — Yes')
    print('[N] — No')
    print('———————————————————————————————————————————————')
    while True:
        choice = input('->').strip().upper()
        if choice == '':
            invalid_input()
        elif choice == 'YES' or choice == 'Y':
            return True
        elif choice == 'NO' or choice == 'N':
            return False
        else:
            invalid_input()
            
#Manager Function//
def check_wpm():
    header()
    print('        W  P  M      C  H  E  C  K  E  R')
    header()
    
    username = username_input()
    print()
    words_typed = words_typed_input()
    print()
    time_minutes = time_minutes_input()
    
    wpm = calculate_wpm(words_typed, time_minutes)
    
    rating = check_rating(wpm)
    
    display_results(username, 
    words_typed, 
    time_minutes, 
    wpm,
    rating)

## -- MAIN PROGRAM --  ##
while True:
    check_wpm()

    if not return_menu():
        break
        
print('Thank you for using our service!')
header()