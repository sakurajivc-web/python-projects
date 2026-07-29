#A prorgam that simulates a parking attendant computing parking fees for vechiles with total earnings.

#header function//
def header():
    print()
    print('————————————————————————————————————————————————————')
    print()
    
#function for invalid input//
def invinput():
    print()
    print('--.Invalid Input! Retry.--')
    print()

print('————————————————————————————————————————————————————')    
print('             A N I M O    P A R K I N G')
print('————————————————————————————————————————————————————')
    
#variables//
total_earnings = 1765

#function for input of name//
def name_input():
    while True:
        print('Enter Full Name:')
        get_name = input('-> ').strip().capitalize().capitalize()
        if get_name == '':
            invinput()
        else:
            return get_name

#function for input of vehicle_type//
def vehicle_type_input():
    while True:
        print('Select Vehicle Type:')
        print('Car  Motorcycle  Truck')
        print('[1]     [2]       [3]')
        get_vehicle_type = int(input('-> '))
        if get_vehicle_type < 1 or get_vehicle_type > 3:
            invinput()
        else:
            return get_vehicle_type

#function for input of parked hours//
def parked_hours_input():
    while True:
        print('Enter Hours Parked:')
        get_parked_hours = int(input('-> '))
        if get_parked_hours <= 0:
            invinput()
        else:
            return get_parked_hours
            
#execution of function for name of vehicle owner//
vehicleowner = name_input()
print()
vehicletype = vehicle_type_input()
print()
hours = parked_hours_input()

#vehicletypes/
if vehicletype == 1:
    vehicle = 'Car'
elif vehicletype == 2:
    vehicle = 'Motorcycle'
elif vehicletype == 3:
    vehicle = 'Truck'
    
#computation and rates/
overtimefee = 0

if hours > 24:
    overtimefee = 250    
elif hours > 12:
    overtimefee = 150
elif hours <= 12:
    overtimefee = 0
    
car_rate = hours * 50 + overtimefee
motorcycle_rate = hours * 25 + overtimefee
truck_rate = hours * 75 + overtimefee   
    
#function for user option to continue or exit//  
def continue_or_exit():
    print('Would you like to continue?')
    print('     Continue   Exit')
    print('       [1]      [2]')
    while True:
        get_answer = int(input('-> '))
        if get_answer == 1:
            return False
        elif get_answer == 2:
            return True
        else:
            invinput()   
 
#function for transaction//
def payment_input():
    global total_earnings
    while True:
        print('Vehicle:', vehicle)
        print('Hours Parked:', hours,"Hours")
        if vehicle == 'Car':
            print()
            print('Please pay the following amount:')
            print()
            print(car_rate, 'PHP')
            get_payment = float(input('-> '))
            if get_payment > car_rate:
                print()
                print('Paid:', get_payment, "PHP")
                print('Change:', get_payment - car_rate, "PHP")
                total_earnings = car_rate + total_earnings
                if continue_or_exit():
                    break
            elif get_payment == car_rate:
                print()
                print('Paid:', get_payment, "PHP")
                total_earnings = get_payment + total_earnings
                if continue_or_exit():
                    break
            elif get_payment < car_rate:
                print()
                print('Insufficient cash Retry!')
                continue
        elif vehicle == 'Motorcycle':
            print()
            print('Please pay the following amount:')
            print(motorcycle_rate, 'PHP')
            get_payment = float(input('-> '))
            if get_payment > motorcycle_rate:
                print()
                print('Paid:', get_payment, "PHP")
                print('Change:', get_payment - motorcycle_rate, "PHP")
                total_earnings = motorcycle_rate + total_earnings
                if continue_or_exit():
                    break
            elif get_payment == motorcycle_rate:
                print()
                print('Paid:', get_payment, "PHP")
                total_earnings = get_payment + total_earnings
                if continue_or_exit():
                    break
            elif get_payment < motorcycle_rate:
                print()
                print('Insufficient cash Retry!')
                continue
        elif vehicle == 'Truck':
            print()
            print('Please pay the following amount:')
            print(truck_rate, 'PHP')
            get_payment = float(input('-> '))
            if get_payment > truck_rate:
                print()
                print('Paid:', get_payment, "PHP")
                print('Change:', get_payment - truck_rate, "PHP")
                total_earnings = truck_rate + total_earnings
                if continue_or_exit():
                    break
            elif get_payment == truck_rate:
                print()
                print('Paid:', get_payment, "PHP")
                total_earnings = get_payment + total_earnings
                if continue_or_exit():
                    break
            elif get_payment < truck_rate:
                print()
                print('Insufficient cash Retry!')
                continue
    print()
    print('Company Total Earnings:', total_earnings, 'PHP')
    
    

    
header()            
payment_input()     
header()
print('Thank you for using Animo Parking!')
                
