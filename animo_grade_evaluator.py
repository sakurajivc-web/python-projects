#A program simulating computation of a student's grade, resulting in remarks.

#function for header//
def header():
    print()
    print('—————————————————————————————————————————————————————————————————————')
    print()

#function for invalid input//
def invalid_input():
    print()
    print('--Invalid Input! Please retry.--')
    
#INPUT functions//-

#student information//

#student name/
def student_name():
    print('Enter Name:')
    while True:
        get_name = input('-> ').strip().title()
        if get_name == '':
            invalid_input()
        else:
            return get_name
            
#student section/
def student_section():
    print('Enter Section:')
    while True:
        get_section = input('-> ').strip().upper()
        if get_section == '':
            invalid_input()
        else:
            return get_section
            
#student program/
student_program_options = ['BSIT', 'BSCPE', 'BSCS']
def student_program():
    print('Enter Student Program:')
    while True:
        get_program = input('-> ').strip().upper()
        if get_program == '':
            invalid_input()
        elif get_program in student_program_options:
            return get_program
        else:
            invalid_input()
            
#grades[reusable]/
def grade_input(subject):
    print('Enter grades in', subject + ':')
    while True:
        get_grade = float(input('-> '))
        if get_grade < 1 or get_grade > 100:
            invalid_input()
        else:
            return get_grade
        
#remarks[reusable/]        
def grade_remark(grade):
    if grade >= 90:
        remarks = 'Excellent'
    elif grade >= 75:
        remarks = 'Passed'
    else:
        remarks = 'Failed'
    
    return remarks
    
#general average computation/      
def general_average(Python, Linux, Networking, Hardware):
    genavg = (Python + Linux + Networking + Hardware) / 4
    return genavg

#general average remarks/    
def general_avg_remarks(grade_average):
    if grade_average >= 98:
        avgremarks = 'With Highest Honors'
    elif grade_average >= 95:
        avgremarks = 'With High Honors'
    elif grade_average >= 90:
        avgremarks = 'With Honors'
    elif grade_average >= 75:
        avgremarks = 'Passed'
    else:
        avgremarks = 'Failed'
    
    return avgremarks
    
#student report output function/
def student_report(name, 
    section, 
    program, 
    Python, 
    Linux, 
    Networking, 
    Hardware, 
    pyremarks, 
    linuxremarks, 
    netwremarks, 
    hardwremarks, 
    grade_average, 
    avgremarks):
    header() 
    print('Student Name:', name)
    print('Student Section:', section)
    print('Student Program:', program)  
    header()
    print('                          G R A D E S')
    header()
    print('Python:', Python)
    print('Remarks:', pyremarks)
    print()
    print('Linux:', Linux)
    print('Remarks:', linuxremarks)
    print()
    print('Networking:', Networking)
    print('Remarks:', netwremarks)
    print()
    print('Hardware:', Hardware)
    print('Remarks:', hardwremarks)
    header()
    print('General Average:', grade_average)
    print('Remarks:', avgremarks)   

#exit or a new set?/
def return_menu():
    header()
    print('Check a new set?')
    print('[Y]')
    print('Exit')
    print('[N]')
    while True:
        choice = input('-> ').strip().upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            invalid_input()
            
## MAIN PROGRAM
def main_program():
    header()
    print(' D E   L A   S A L L E   U N I V E R S I T Y   D A S M A R I N A S')
    print('                   S T U D E N T    R E P O R T')
    header()
    name = student_name()
    print()
    section = student_section()
    print()
    program = student_program()
    header()
    Python = grade_input('Python')
    print()
    Linux = grade_input('Linux')
    print()
    Networking = grade_input('Networking')
    print()
    Hardware = grade_input('Hardware')

    pyremarks = grade_remark(Python)
    linuxremarks = grade_remark(Linux)
    netwremarks = grade_remark(Networking)
    hardwremarks = grade_remark(Hardware)

    grade_average = general_average(Python, Linux, Networking, Hardware)

    avgremarks = general_avg_remarks(grade_average)

    student_report(name, 
    section, 
    program, 
    Python, 
    Linux, 
    Networking, 
    Hardware, 
    pyremarks, 
    linuxremarks, 
    netwremarks, 
    hardwremarks, 
    grade_average, 
    avgremarks)

while True:
    main_program()
    
    if not return_menu():
        break
#ending//
header()
print('            A N I M O   L A  S A L L E  !')
header()