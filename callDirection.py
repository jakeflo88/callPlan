# FOR DIRECTING CALL TRAFFIC
import random


# Call comes in
call = ''

# Good morning, Thistle Hyundai computer speaking, how can I direct your call?
print('Good morning, Thistle Hyundai, this is computer speaking.\n\nHow can I direct your call?')

call = input()


# Sales call
if call.lower() ==  'sales':

    print('Thanks, please hold for just a moment and I will see who is available\n')
    print('***Places on HOLD***')
    
    print('***Announce on PA or just look to see***\n')

    availableSales = random.randint(0, 9)

    if availableSales >= 5:
        print('Jake is available\n')
        print('***Call is sent to Jake***\n\n')

        print('Good morning, Thistle Hyundai, Jake speaking!')
        

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

#############################################


# Service call

# TODO
# Appointment (common) - Amber/Mandy)?
# Breakdown (rare) - Place on hold - Go find someone to pickup!
# Update - Switch to direct call
# Warranty - Switch to direct call
# General inquiry - Ring all - Voicemail or flip back to reception?
# Perhaps these can be divided into direct calls and appointments?

#############################################


# Parts
if call.lower() == 'parts':

    print('Thanks, I will connect you to the parts department\n')

    availableParts = random.randint(0, 9)

    if availableParts >= 5:
        print('Good morning, parts department speaking!')

    else:
        print('Our parts department are currently assisting other customers/nPress 1 to leave a message that will be responded to ASAP')
        


# Direct call
if call.lower() == 'direct':

    print('Thanks, I will connect you directly\n')

    availableDirect = random.randint(0, 9)

    if availableDirect >= 5:
        print('Hello, you have reached me directly!')

    else:
        print('Direct is unavailable..\nPress 1 to record a voicemail\nPress 2 to be connected to the next available department member')
        
#Lunch mode
        #Service press 1, Sales press 2, Parts press 3
        #Ring all
        #Or just have someone on the desk

#After 5
        #Ring all sales

#After close
        #I think is already handled, but let's find out
