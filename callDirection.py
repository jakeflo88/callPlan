# FOR DIRECTING CALL TRAFFIC

# TODO
# Accurate time-based random chance would be fun and cool but not necessary for now



# Call comes in, answer?
print('Ring ring..')
call = input()

# Automated system
if call.lower() == 'n':

    # for this part option 1 is redundant
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
        print('''Welcome to the Service Department:\n
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

    # for general sales inquiries press 1?
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
    print('Good morning, Thistle Hyundai, this is reception speaking.\n\nHow can I direct your call?')

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
            
            print('***Announce on PA or just look to see***')

            availableSales = input()

            if availableSales == 'y':
                print('Jake is available\n')
                print('***Call is sent to Jake***\n\n')

                print('Good morning, Thistle Hyundai, Jake speaking!')
                

            elif availableSales == 'n':
                print('No one is available\n')
                print('*Takes name and number, will call you back*')


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

        # Perhaps all of these service calls can be divided into direct calls and appointments?
        # ^UPDATE generally yes



    # Parts
    if call.lower() == 'parts':

        print('\nThanks, I will connect you to the parts department..')

        availableParts = input()

        if availableParts == 'y':
            print('Good morning, parts department speaking!')

        elif availableParts == 'n':
            print('Our parts department are currently assisting other customers.\nPlease leave a message that will be responded to ASAP')
            


    # Direct call
    if call.lower() == 'direct':

        print('\nConnecting you directly..')

        availableDirect = input()

        if availableDirect == 'y':
            print('Hello, you have reached me directly!')

        elif availableDirect == 'n':
            print('Hi, you have reached my personal voicemail')
        
        
#Lunchtime
        # just have someone on the desk really


