#A program simulating checking a user's internet speed and classifying the conenction quality.

#Uitlity Functions//

#header-
def header():
    print()
    print('——————————————————————————————————————————————')
    print()
    
#invalid input-
def invalid_input():
    print()
    print('——Invalid Input! Please Retry.——')
        
#Input Functions//

#download speed-
def download_speed_input():
    print('Enter Download Speed [MBPS]:')
    while True:
        try:
            get_dl_speed = int(input('-> '))
            if get_dl_speed < 0:
                invalid_input()
            else:
                return get_dl_speed
        except ValueError:
            invalid_input()
            
#upload speed-
def upload_speed_input():
    print('Enter Upload Speed [MBPS]:')
    while True:
        try:
            get_upl_speed = int(input('-> '))
            if get_upl_speed < 0:
                invalid_input()
            else:
                return get_upl_speed
        except ValueError:
            invalid_input()
            
#ping-
def ping_input():
    print('Enter Ping [ms]:')
    while True:
        try:
            get_ping = int(input('-> '))
            if get_ping < 0:
                invalid_input()
            else:
                return get_ping
        except ValueError:
            invalid_input() 

#Processing functionn//
def wifi_speed_classification(dl_speed, upl_speed, ping):
    if dl_speed >= 100 and upl_speed >= 75 and ping <= 20:
        quality_classification = 'Excellent — ★★★★★'
    elif dl_speed >= 75 and upl_speed >= 50 and ping <= 50:
        quality_classification = 'Good — ★★★★☆'
    elif dl_speed >= 50 and upl_speed >= 30 and ping <= 80:
        quality_classification = 'Average — ★★★☆☆'
    else:
        quality_classification = 'Poor — ★★☆☆☆'

    return quality_classification

#Output functions//

#wifi speed report-
def wifi_speed_report(dl_speed, 
    upl_speed, 
    ping, 
    quality):
    header()
    print('     W I — F I    S P E E D    R E P O R T')
    header()
    print('Download Speed:', dl_speed, 'Mbps')
    print('Upload Speed:', upl_speed, 'Mbps')
    print('Ping:', ping, 'ms')
    print()
    print('Internet Quality:', quality)
    header()
    
#check again or exit?
def return_menu():
    print('Would you like to re-check?')
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
def check_wifi_speed():
    header()
    print('     W I — F I    S P E E D    C H E C K E R')
    header()
    
    dl_speed = download_speed_input()
    print()
    upl_speed = upload_speed_input()
    print()
    ping = ping_input()
    
    quality = wifi_speed_classification(dl_speed, upl_speed, ping)
     
    wifi_speed_report(dl_speed, 
    upl_speed, 
    ping, 
    quality)

## -- MAIN PROGRAM -- ##
while True:
    check_wifi_speed()

    if not return_menu():
        break

print('Thank you for using our Wi-Fi Speed Analysis!')
header()