#A simple program where filename input of the user tells them what type of file it is.

## Utilities

import time

def header():
    print()
    print('—————————————————————————————————————————————')
    print()
    
def invalid_input():
    print()
    print('——Invalid input! Please retry.——')
        
## Input Function

# Get filename from user /
def filename_input():
        filename_input = input('Enter filename: -> ').strip().lower()
        return filename_input
    
## Processing Function

# Check type and extension of file
def determine_filetype_extension(filename):
    if filename == 'txt':
        filetype = 'Text File'
        extension = '.txt'
    elif filename == 'doc' or filename == 'docx':
        filetype = 'Word Document'
        extension = '.doc / .docx'
    elif filename == 'pdf':
        filetype = 'PDF Document'
        extension = '.pdf'
    elif filename == 'xls' or filename == 'xlsx':
        filetype = 'Excel Spreadsheet'
        extension = '.xls / .xlsx'
    elif filename == 'ppt' or filename == 'pptx':
        filetype = 'PowerPoint Presentation'
        extension = '.ppt / .pptx'
    elif filename == 'py':
        filetype = 'Python File'
        extension = '.py'
    elif filename == 'java':
        filetype = 'Java File'
        extension = '.java'
    elif filename == 'jpg' or filename == 'jpeg':
        filetype = 'JPEG Image'
        extension = '.jpg / .jpeg'
    elif filename == 'png':
        filetype = 'PNG Image'
        extension = '.png'
    elif filename == 'gif':
        filetype = 'GIF Image'
        extension = '.gif'
    elif filename == 'mp3':
        filetype = 'MP3 Audio'
        extension = '.mp3'
    elif filename == 'mp4':
        filetype = 'MP4 Video'
        extension = '.mp4'
    else:
        filetype = 'Unsupported'
        extension = 'Unsupported'    
    
    return filetype, extension
    
## Output Functions

# Show results /
def display_results(filename, filetype, extension):
    header()
    print('Filename: ', filename)
    time.sleep(1)
    print()
    print('File Type: ', filetype)
    time.sleep(0.7)
    print('Extension: ', extension)
    time.sleep(0.7)
    
# Try again? /
def return_menu():
    print('Would you like to try again? ')
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
def simulate_checking():
    header()
    filename = filename_input()
    filetype, extension = determine_filetype_extension(filename)
    
    if '.' in filename:
        extension = filename.split('.')[-1]
    else:
        extension = ''
    
    display_results(filename, filetype, extension)
    
## -- MAIN PROGRAM -- ##
while True:
    simulate_checking()
    
    if not return_menu():
        break
        
print('Thank you for using our program!')
header() 