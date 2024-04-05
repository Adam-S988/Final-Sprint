## DESCRIPTION: Main Menu for 5 Python Programs / Sprint 1
## DATE CREATED: 03/29/2024
## GROUP: Nine

import Functions as FV
import SnFunctions as SN

defaults = FV.read_defaults()


### MAIN MENU ###
def main_menu():
    while True:
        
        print(f"                   /\_______________________________________/\ ")
        print(f"                   ||~~~~~~~~~~ HAB Taxi Services ~~~~~~~~~~||")
        print(f"                   ||        Company Services System        ||")
        print(f"                   ||                  :::                  ||")
        print(f"                   ||               Main Menu               ||")
        print(f"                   ||_______________________________________||")
        print(f"                                       |||")
        print(f"||----||-------------------------------|||")
        print(f"|| #1 || Enter a New Employee (Driver) |||")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"                                       ||| #2 || Enter Company Revenues        ||")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"|| #3 || Enter Company Expenses        ||| ")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"                                       ||| #4 || Track Car Rentals.            ||")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"|| #5 || Record Employee Payment       |||")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"                                       ||| #6 || Print Company Profit Listing  ||")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"|| #7 || Print Driver Financial Listing|||                                       ")
        print(f"||----||-------------------------------|||----||-------------------------------||")
        print(f"                                       ||| #8 || Your report - placeholder     ||")
        print(f"                                       |||----||-------------------------------||")
        print(f"                                       |||                                       ")
        print(f"                       |----|----------------------|----|")
        print(f"                       | #9 |  -- EXIT PROGRAM --  | #9 |")
        print(f"                       |----|----------------------|----|")
        print()              
        print(f" ____________________________________")
        print(f"|                                    |")
        print(f"|---- Enter your choice #(1 - 9) ----|")
        print(f"|____________________________________|")
        choice = input("     #")
        
        if choice == '1':
            program1()
        elif choice == '2':
            program2()
        elif choice == '3':
            program3()
        elif choice == '4':
            program4()
        elif choice == '5':
            program5()
        elif choice == '6':
            program6()
        elif choice == '7':
            program7()        
        elif choice == '8':
            program8()
        elif choice == '9':
            print("EXITING PROGRAM")
            break
        else:
            print("INVALID CHOICE, PLEASE TRY AGAIN.")



### COMPANY PROGRAMS ###

# Enter a New Employee (driver)
def program1():
    '''
    Enter a New Employee (driver), updating defaults.dat and saving to Employees.txt
    '''
    print()
    print()
    print()

  # Read default settings, specifically looking for the next available driver number
    global defaults

    while True:        
        next_driver_number = int(defaults['Next driver number'])
        print(f"______________________________")
        print()
        print(f"---NOW CREATING PROFILE---")
        print(f" --DRIVER NUMBER # {next_driver_number}--")
        print(f"______________________________")

    # Collect user information through the employee functions module
        user_info = SN.collect_user_info(str(next_driver_number))
        license_info = SN.collect_and_validate_drivers_license(user_info)
                
    # Update user_info with license information and the next driver number
        user_info.update(license_info)
        user_info['driver_number'] = str(next_driver_number) # Store driver_number in user_info as a string

    # Add starting balance of $0 to the file
        user_info['balance'] = 0
        user_info['balance'] = str(user_info['balance']) # Convert to a string for saving


    # Show entered info to user, ask them to confirm before saving or start over.
        print(user_info)
        for key, value in user_info.items():
            print(f"|-{key:>22s} -- {value:<33s}-|")
    
        print(f"PLEASE REVIEW THE EMPLOYEE DATA BEFORE SAVING.")
        Save_confirmation = FV.prompt_and_validate(
            "SAVE EMPLOYEE DATA? (Y/N):  ",
            "yes_no",
            "PLEASE ENTER Y TO INDICATE YES. ENTER N TO INDICATE NO."
            )
        
        # Saving Data Process
        if Save_confirmation.lower() =='y':
            
        # Prepare for the next employee by incrementing the driver number
            next_driver_number += 1
            defaults['Next driver number'] = str(next_driver_number)
                    
        # Write updated defaults back to file
            FV.write_defaults(defaults)    
                    
        # Append the new employee's information to Employees.dat
            SN.append_employee_data(user_info, filename="Employees_test.txt")
            print(f"--- SUCCESS!! ---")
            print(f" DEFAULT SETTINGS SUCCESFULLY UPDATED AND SAVED TO  Defaults.dat !")
            print(f" EMPLOYEE DATA FOR EMPLOYEE #{user_info['driver_number']}: {user_info['first_name']} {user_info['last_name']}, HAS BEEN SUCCESFULLY SAVED TO  Employees.txt !")
            print()
            # Ask if the user wants to input another employee
            if user_info.get('owns_car', 'Y').lower() == 'n':  # Check if user does not own a vehicle
                continue_to_program4 = FV.prompt_and_validate(
                    "CONTINUE TO TRACK CAR RENTALS? (Y/N): ",
                    "yes_no",
                    "PLEASE ENTER Y TO CONTINUE TO TRACK CAR RENTALS. ENTER N TO SKIP."
                    )
                if continue_to_program4.lower() == 'y':
                    program4()                    
            
            add_another = FV.prompt_and_validate(
                "WOULD YOU LIKE TO CREATE ANOTHER EMPLOYEE FILE? (Yes/no as Y/N): ",
                "yes_no",
                "PLEASE ENTER Y TO INDICATE YES. ENTER N TO INDICATE NO."
                )
                    
            if add_another.lower() != 'y':
                        print()
                        print("RETURNING TO MAIN MENU...")
                        print()
                        break  # Exiting the loop to return to the main menu
        else:
            # If the user decides not to save, they're prompted to confirm starting over or returning to the main menu
            print()
            restart_or_menu = FV.prompt_and_validate(
                "START OVER WITH A NEW EMPLOYEE FILE? (Y/N): ",
                "yes_no",
                "PLEASE ENTER Y TO INDICATE YES. ENTER N TO INDICATE NO."
            )
            if restart_or_menu.lower() != 'y':
                print("RETURNING TO MAIN MENU...")
                break  # Exit the loop to return to the main menu

# Enter Company Revenues.
def program2():
    print()
    print("placeholder2")
    print()

# Enter Company Expenses.
def program3():
    print()
    print("placeholder3")
    print()

# Track Car Rentals.
def program4():
    print()
    print("placeholder4")
    print()

# Record Employee Payment.    
def program5():
    print()
    print("placeholder5")
    print()

# Print Company Profit Listing
def program6():
    print()
    print("placeholder6")
    print()

# Print Driver Financial Listing.
def program7():
    print()
    print("placeholder7")
    print()

# Your report - add description here.
def program8():
    print()
    print("placeholder8")
    print()



#RUNS MAIN MENU IF THIS FILE IS INITIALIZED
if __name__ == "__main__":
    main_menu()


