# FOR DIRECTING CALL TRAFFIC
import random


# Call comes in
call = ''

# Good morning, Thistle Hyundai computer speaking, how can I direct your call?
print('Good morning, Thistle Hyundai computer speaking, how can I direct your call?')

call = input()



# Sales call
if call ==  'sales':
    
    print('Thanks, I will connect you to the sales department\n')
    
    print('*Announce on PA or just look to see*\n')

    availableSales = random.randint(0, 9)

    if availableSales >= 5:
        print('Jake is available\n')
        print('Call is sent to Jake')

    else:
        print('No one is available\n')
        print('*Takes name and number, will call you back*')

# THIS IS WHAT IS HAPPENING NOW   
#    print('Sales phone, "Ring ring Sales ring.."\n')
#
#    pickup = random.randint(0, 9)
#
#   if pickup >= 5:
#       print('Hello! Would you like to buy a car?')
#
#   else:
#       print('No answer -> goes to directly to voicemail.\n')


# Service call

# Parts

# Direct call
if call == 'direct':

    print('Thank, I will connect you directly\n')

    availableDirect = random.randint(0, 9)

    if availableDirect >= 5:
        print('Hello, you have reached me directly!')

    else:
        print('Direct is unavailable..\nPress 1 to record a voicemail\nPress 2 to be connected to the next available department member')
        

#
