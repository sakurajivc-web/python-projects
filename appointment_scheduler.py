#A tiny program where the user enters an appointment's day and time, then the program checks whether the appointment is during your allowed hours an days. 

# Utilities /

def header():
    print()
    print('———————————————————————————————————————————————————————')
    print()
    
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')

## Input Functions
                
def hour_input():
    print('Select Hour:')
    print('[0-23]')
    while True:
        try:
            choice = int(input('-> '))
            if choice < 0 or choice > 23:
                invalid_input()
            else:
                return choice
        except ValueError:
            invalid_input()
            
## Processing Functions

def convert_to_hour(selected_time):
    if selected_time == 0:
        hour = '12:00 AM'
    elif selected_time == 1:
        hour = '1:00 AM'
    elif selected_time == 2:
        hour = '2:00 AM'
    elif selected_time == 3:
        hour = '3:00 AM'
    elif selected_time == 4:
        hour = '4:00 AM'
    elif selected_time == 5:
        hour = '5:00 AM'
    elif selected_time == 6:
        hour = '6:00 AM'
    elif selected_time == 7:
        hour = '7:00 AM'
    elif selected_time == 8:
        hour = '8:00 AM'
    elif selected_time == 9:
        hour = '9:00 AM'
    elif selected_time == 10:
        hour = '10:00 AM'
    elif selected_time == 11:
        hour = '11:00 AM'
    elif selected_time == 12:
        hour = '12:00 PM'
    elif selected_time == 13:
        hour = '1:00 PM'
    elif selected_time == 14:
        hour = '2:00 PM'
    elif selected_time == 15:
        hour = '3:00 PM'
    elif selected_time == 16:
        hour = '4:00 PM'
    elif selected_time == 17:
        hour = '5:00 PM'
    elif selected_time == 18:
        hour = '6:00 PM'
    elif selected_time == 19:
        hour = '7:00 PM'
    elif selected_time == 20:
        hour = '8:00 PM'
    elif selected_time == 21:
        hour = '9:00 PM'
    elif selected_time == 22:
        hour = '10:00 PM'
    else:
        hour = '11:00 PM'
        
    return hour
    
def status_check(selected_time):
    if selected_time <= 8 or selected_time >= 17:
        return "Outside Operation Hours"
    else:
        return 'Available'
        
## Output Functions

def display_appointment(hour, status):
    print()
    print('Appointment:', hour) 
    print('Status:', status)
    
def return_menu():
    print('Would you like to try again?')
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
            
## Manager Function
def simulate_appointment_sched():
    header()
    print('       A P P O I N T M E N T   C H E C K E R')
    header()
    
    selected_time = hour_input()
    
    hour = convert_to_hour(selected_time)
    status = status_check(selected_time)
    
    display_appointment(hour, status)
    header()
    
## -- MAIN PROGRAM -- ##
while True:
    simulate_appointment_sched()
    
    if not return_menu():
        break
        
print('An apple a day, keeps the doctor away.')
header()        