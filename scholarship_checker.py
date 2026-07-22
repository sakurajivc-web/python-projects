#A program that determines whether a student is eligible for a scholarship based on their general average and family income.

#function for header//
def header():
    print()
    print('——————————————————————————————————————————————————————')
    print()

#function for invalid_input//
def invalid_input():
    print()
    print('--Invalid Input! Please retry.--')
    
#Input functions//

#name input-
def name_input():
    print('Enter Name:')
    while True:
        get_name = input('-> ').strip().title()
        if get_name == '':
            invalid_input()
        else:
            return get_name
            
#program input-
def program_input():
    print('Enter College Program:')
    while True:
        get_program = input('-> ').strip().upper()
        if get_program == '':
            invalid_input()
        else:
            return get_program
            
#grade input - [reusable function]
def grade_input(subject):
    print('Enter Grade in:', subject)
    while True:
        try:
            get_grade = float(input('-> '))
            if get_grade <= 0 or get_grade > 100:
                invalid_input()
            else:
                return get_grade
        except ValueError:
            invalid_input()
            
#family income input-
def family_income_input():
    print('Enter Monthly Family Income:')
    while True:
        try:
            get_income = int(input('-> '))
            if get_income < 0:
                invalid_input()
            else:
                return get_income
        except ValueError:
            invalid_input()
            
#Processing functions//
#computation for general average
def general_average(python_grade, linux_grade, networking_grade, hardware_grade):
    gen_avg_computation = (python_grade + linux_grade + networking_grade + hardware_grade) / 4
    return gen_avg_computation
 
#processing for scholarship eligbility   
def scholarship_eligibility(general_avg, family_monthly_income):
    if general_avg >= 95 and family_monthly_income <= 40000:
        eligibility = 'Full Scholarship'
    elif general_avg >= 90 and family_monthly_income <= 70000:
        eligibility = 'Partial Scholarship'
    else:
        eligibility = 'Not Eligible'
    
    return eligibility
    
#Output functions//
def scholarship_result(student_name, 
    student_program, 
    python_grade, 
    linux_grade, 
    networking_grade, 
    hardware_grade, 
    general_avg,
    family_monthly_income, 
    scholarship_status):
    header()
    print('   A N I M O   S C H O L A R S H I P   C H E C K E R')
    header()
    print('Student:', student_name)
    print('Program:', student_program)
    header()
    print('           S U B J E C T S   G R A D E S')
    header()
    print('Python:', python_grade)
    print('Linux:', linux_grade)
    print('Networking:', networking_grade)
    print('Hardware:', hardware_grade)
    header()
    print('General Average:', general_avg)
    print()
    print('Family Montly Income:', family_monthly_income, "PHP")
    header()
    print('Scholarship Staus:', scholarship_status)
    header()       

#Exit or continue?/
def return_menu():
    print('Recheck Eligibility?')
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
            
#Main Program Function//
def scholarship_checker():
    header()
    student_name = name_input()
    print()
    student_program = program_input()
    header()
    python_grade = grade_input('Python')
    print()
    linux_grade = grade_input('Linux')
    print()
    networking_grade = grade_input('Networking')
    print()
    hardware_grade = grade_input('Hardware')
    header()
    family_monthly_income = family_income_input()
    
    general_avg = general_average(python_grade, 
        linux_grade, 
        networking_grade, 
        hardware_grade)
    print()
    scholarship_status = scholarship_eligibility(general_avg, family_monthly_income)
    
    scholarship_result(student_name, 
    student_program, 
    python_grade, 
    linux_grade, 
    networking_grade, 
    hardware_grade, 
    general_avg,
    family_monthly_income, 
    scholarship_status)

# -- MAIN PROGRAM -- ##
while True:
    scholarship_checker()
    
    if not return_menu():
        break
        
print('Padayon! Goodluck on your journey! Keep fighting!')
header()



















    




