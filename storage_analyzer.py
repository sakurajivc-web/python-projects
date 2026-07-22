#A program that checks how much storage is used on a computer and dtermines its storage status.

#function for header//
def header():
    print()
    print('———————————————————————————————————————————————————————————————')
    print()
    
#function for invalid input//    
def invalid_input():
    print()
    print('--Invalid Input! Please retry.--')
    
#functions for input//
#name-
def name_input():
    print('Enter Name:')
    while True:
        get_name = input('-> ').strip().title()
        if get_name == '':
            invalid_input()
        else:
            return get_name
            
#computer model-
def model_input():
    print('Enter Computer Model:')
    while True:
        get_model = input('-> ').strip().title()
        if get_model == '':
            invalid_input()
        else:
            return get_model
            
#total storage-
def total_s_input():
    while True:
        try:
            print('Enter Total Storage of Computer: [GB]')
            get_total_s = float(input('-> '))
            if get_total_s < 32:
                invalid_input() 
            elif get_total_s > 5000:
                invalid_input()
            else:
                return get_total_s
        except ValueError:
            invalid_input()

#used storage-
def used_s_input():
    while True:
        try:
            print('Enter Used Storage of Computer: [GB]')
            get_used_s = float(input('-> '))
            if get_used_s < 32:
                invalid_input() 
            elif get_used_s > 5000:
                invalid_input()
            else:
                return get_used_s
        except ValueError:
            invalid_input()
            
#functions for processing
#computation of input-
def computation_percentage(total_storage, used_storage):
    storage_used_pct = (used_storage / total_storage) * 100
    return storage_used_pct
def computation_free(total_storage, used_storage):
    free_storage_calc = total_storage - used_storage
    return free_storage_calc

#classification of computation
def computation_classification(storage_usage):
    if storage_usage <= 50:
        classification = 'Plenty of Storage'
    elif storage_usage <= 80:
        classification = 'Moderate Usage'
    elif storage_usage <= 98:
        classification = 'Almost Full'
    else:
        classification = 'Full'
    
    return classification

    
#function for output display//
def ouput(customer, 
    model, 
    total_storage, 
    used_storage, 
    free_storage, 
    storage_usage, 
    status): 
    header()
    print('      A N I M O    S T O R A G E    A N A L Y Z E R')
    header()
    print('Customer:', customer)
    print('Computer Model:', model)
    header()
    print('Designed Storage:', total_storage, 'GB')
    print('Used Storage:', used_storage, 'GB')
    print('Free Storage:', free_storage, 'GB')
    print('Storage Usage:', storage_usage, "%")
    header()
    print('Status:', status)
    header()

#continue or exit? - function    
def return_menu():
    print('Check a new computer?')
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
   
#manager function//
def check_computer():
    header()
    customer = name_input()
    print()
    model = model_input()
    print()
    total_storage = total_s_input()
    print()
    used_storage = used_s_input()
    print()
    free_storage = computation_free(total_storage, used_storage)
    storage_usage = computation_percentage(total_storage, used_storage)
    status = computation_classification(storage_usage)
    ouput(customer, 
    model, 
    total_storage, 
    used_storage, 
    free_storage, 
    storage_usage, 
    status)

# -- MAIN PROGRAM EXECUTION -- #
while True:
    check_computer()
    
    if not return_menu():
        break
header()
print('Take good care of your storage. Goodbye! Animo La Salle!')   
         











