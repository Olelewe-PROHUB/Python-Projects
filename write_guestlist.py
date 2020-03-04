#Similar to the program write_guestlist.py
#Changes include the addition of a question

filename = 'prgm_poll.txt'

answer = ''

with open(filename, 'w') as file_object:

    while answer != 'c': 
        answer = input('Why do you like programming? (Enter "c" to cancel): ')
        
        if answer != 'c':
            file_object.write(f"{answer}!\n")
            continue
        else:
            break 

