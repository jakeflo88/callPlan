# FOR DIRECTING CALL TRAFFIC

# TODO
# Go through automated call system after hours and integrate
# Remove random chance and change to directions
# Eventually set up more accurate time-based random chance

import random


# Call comes in, answer?
print('Ring ring..')
call = input()

# Automated system
if call.lower() == 'n':

    print('''Welcome to Thistle Hyundai, for:\n 
    Reception - Press 1\n
    Service - Press 2\n
    Parts - Press 3\n
    Sales - Press 4\n
    Staff Directory - Press 5\n''')

    choice = input()

    if choice == '1':
        print('Reception phone is now ringing..')

    elif choice == '2':
        print('''Welcome to the Servive Department:\n
        To book an appointment - Press 1\n
        To check on the status of your vehicle - Press 2\n
        Questions about warranty - Press 3\n
        To speak to the service manager - Press 4\n
        For information on how to book online - Press 5\n''')

        serviceChoice = input()

        if serviceChoice == '1':
            print('Connect to Amber/Mandy')

        elif serviceChoice == '2':
            print('Connect to service bank')

        elif serviceChoice == '3':
            print('Connect to Eric?')

        elif serviceChoice == '4':
            print('Connect to Sherry')

        elif serviceChoice == '5':
            print('Go to thistlehyundai.com, etc. etc.')

    elif choice == '3':
        print('Connect to parts')

    elif choice == '4':
        print('''Welcome to the sales department, for:\n
        Jeremy Watkins - Press 1\n
        Zack Saulnier - Press 2\n
        Jordan Newcombe - Press 3\n
        Jake Florian - Press 4\n
        Jessica Leblanc - Press 5\n''')

    elif choice == '5':
        print('Connect to entire staff directory')



# for someone actually picking up
elif call.lower() == 'y':

    # Good morning, Thistle Hyundai computer speaking, how can I direct your call?
    print('Good morning, Thistle Hyundai, this is computer speaking.\n\nHow can I direct your call?')

    call = input()

    # Sales call
    if call.lower() ==  'sales':

        print('\nHave you been speaking with someone already?')

        responseSales = input()

        if responseSales.lower() == 'yes':
            call = 'direct'

        else:

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
    if call.lower() == 'service':
        
        # Appointment (common) - Amber/Mandy)?
        print('\nAre you looking to book or change an appointment?')

        responseService = input()

        if responseService.lower() == 'yes':
            print('\nNo problem, I will connect you to the booking department\n')
            call = 'direct'

        # Breakdown (rare) - Place on hold - Go find someone to pickup!
        elif responseService.lower() == 'breakdown':
            print('\nPlease hold for a moment while I find someone to help you immediately')
            print('***Place on hold and find someone to pick up the phone***')

        # Update - Switch to direct call
        elif responseService.lower() == 'update':
            call = 'direct'

        else:
            print('Let me take down your name and number, and we will get back to you shortly')

        # TODO
        # General inquiry - Ring all? - Voicemail? - or flip back to reception?
        # Perhaps all of these service calls can be divided into direct calls and appointments?
        # ^UPDATE generally yes

    #############################################


    # Parts
    if call.lower() == 'parts':

        print('\nThanks, I will connect you to the parts department..\n')

        availableParts = random.randint(0, 9)

        if availableParts >= 5:
            print('Good morning, parts department speaking!')

        else:
            print('Our parts department are currently assisting other customers.\nPlease leave a message that will be responded to ASAP')
            


    # Direct call
    if call.lower() == 'direct':

        print('\nConnecting you directly..\n')

        availableDirect = random.randint(0, 9)

        if availableDirect >= 5:
            print('Hello, you have reached me directly!')

        else:
            print('Direct is unavailable..\nPress 1 to record a voicemail\nPress 2 to be connected to the next available department member')
            # Will need to ask Norman about ring all features
        
        
#Lunchtime
        #just have someone on the desk really

#After 5pm
        # Ring all sales

#After close
        # I think is already handled, but let's find out


