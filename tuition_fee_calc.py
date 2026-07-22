#A program that simulates a student enrolling in a semester and calculates the total tuition fee based on the number of enrolled units, cost per unit, and miscellaneous fees.

#Utility functions//
def header():
    print()
    print('—————————————————————————————————————————————————————————')
    print()
    
def invalid_input():
    print()
    print('--Invalid Input! Please retry.--')
    
#Input functions//

#name-
def name_input():
    print('Enter Name:')
    while True:
        get_name = input('-> ').strip().title()
        if get_name == '':
            invalid_input()
        else:
            return get_name
            
#program-
cics_programs = ['BSCS', 'BSCPE', 'BSIT']
def program_input():
    print('Select your program:')
    print('[BSCS, BSCPE, BSIT]')
    while True:
        get_program = input('-> ').strip().upper()
        if get_program in cics_programs:
            return get_program
        else:
            invalid_input()
            
#year level-
def year_level_input():
    print('Enter Year Level:')
    while True:
        try:
            get_year = int(input('-> '))
            if get_year <= 0 or get_year > 5:
                invalid_input()
            else:
                return get_year
        except ValueError:
            invalid_input()
 
#units-
def units_input():
    print('Enter amount of Units:')
    while True:
        try:
            get_units = int(input('-> '))
            if get_units < 12 or get_units > 31:
                invalid_input()
            else:
                return get_units
        except ValueError:
            invalid_input()              

#cost per unit-
def cost_per_unit_input():
    print('Enter Cost Per Unit: [PHP]')
    while True:
        try:
            get_cpu = int(input('-> '))
            if get_cpu < 0 or get_cpu > 50000:
                invalid_input()
            else:
                return get_cpu
        except ValueError:
            invalid_input()

#miscellaneous fee-
def miscellaneous_fee_input():
    print('Enter Miscellaneous Fee Amount: [PHP]')
    while True:
        try:
            get_mfa = int(input('-> '))
            if get_mfa < 0 or get_mfa > 100000:
                invalid_input()
            else:
                return get_mfa
        except ValueError:
            invalid_input()

#Processing functions//

#Tuition Fee-
def compute_tuition_fee(units, cost_per_unit):
    tuition_fee_computation = units * cost_per_unit
    return tuition_fee_computation
       
#Total Fee-
def compute_total_fee(tuition_fee, miscellaneous_fee):
    total_fee_computation = tuition_fee + miscellaneous_fee
    return total_fee_computation
        
#Fee Classification-
def fee_classification(total_fee):
    if total_fee <= 20000:
        status = 'Affordable'
    elif total_fee <= 40000:
        status = 'Standard'
    else:
        status = 'Expensive'
        
    return status

#Output function//

#Summary display-
def tuition_summary(student_name, 
    student_program, 
    year_level, 
    units, 
    cost_per_unit, 
    tuition_fee, 
    miscellaneous_fee, 
    total_fee, 
    classification):
    header()
    print('              R  E  S  U  L  T')
    header()
    print('Student:', student_name)
    print('Program:', student_program)
    print('Year Level:', year_level)
    header()
    print('Units:', units)
    print('Cost per Unit:', cost_per_unit)
    print()
    print('Tuition Fee:', tuition_fee, 'PHP')
    print('Miscellaneous Fee:', miscellaneous_fee, 'PHP')
    header()
    print('Total Fee:', total_fee, 'PHP')
    print()
    print('Classification:', classification)
    header()
    

#Check new tuition or exit?-
def return_menu():
    print('Check another tuition fee?')
    print('[Y] - Yes')
    print('[N] - No')
    while True:
        choice = input('-> ').strip().upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            invalid_input()
            continue
            
#Manager Function for Main Program-
def calculate_tuition_fee():
    header()
    print('   A N I M O    T U I T I O N    C H E C K E R')
    header()
    student_name = name_input()
    print()
    student_program = program_input()
    print()
    year_level = year_level_input()
    header()
    units = units_input()
    print()
    cost_per_unit = cost_per_unit_input()
    print()
    miscellaneous_fee = miscellaneous_fee_input()
    
    tuition_fee = compute_tuition_fee(units, cost_per_unit)
    total_fee = compute_total_fee(tuition_fee, miscellaneous_fee)
    classification = fee_classification(total_fee)
    
    tuition_summary(student_name, 
    student_program, 
    year_level, 
    units, 
    cost_per_unit, 
    tuition_fee, 
    miscellaneous_fee, 
    total_fee, 
    classification)
    
## -- MAIN PROGRAM -- ##
while True:
    calculate_tuition_fee()
    
    if not return_menu():
        break

header()
print('Thank you for using Animo Tuition Checker!')
header()













