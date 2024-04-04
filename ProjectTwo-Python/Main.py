## DESCRIPTION: Main Menu for 5 Python Programs / Sprint 1
## DATE CREATED: 03/29/2024
## GROUP: Nine

import Functions as FV
import SnFunctions as SN

defaults = FV.read_defaults()


### EMPTY MAIN MENU ###
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
       
        
        
        choice = input("Enter your choice (1-9): ")
        
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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")



### EMPTY PROGRAMS ###

# Enter a New Employee (driver)
def program1():
    print()
    print()
    print()

# Read default settings, specifically looking for the next available driver number
    global defaults

    while True:        
        next_driver_number = int(defaults['Next driver number'])
        print(f"______________________________")
        print()
        print(f"---NOW CREATING PROFILE FOR---")
        print(f" --DRIVER NUMBER -- #{next_driver_number}--")
        print(f"______________________________")

    # Collect user information through the employee functions module
        user_info = SN.collect_user_info()
        license_info = SN.collect_and_validate_drivers_license(user_info)
                
    # Update user_info with license information and the next driver number
        user_info.update(license_info)
        user_info['driver_number'] = next_driver_number

    # Show entered info to user, ask them to confirm before saving or start over.
        print(user_info)
        for key, value in user_info.items():
            print(f"|-{key:>22s} -- {value:<33s}-|")
    
        print(f"Please review your Employee data before submitting.")
        Save_confirmation = FV.prompt_and_validate(
            "Save Employee data? (Y/N):  ",
            "yes_no",
            "Please Enter Y for YES and N for No."
            )
        
        if Save_confirmation.lower() =='y':
            
        # Prepare for the next employee by incrementing the driver number
            next_driver_number += 1
            defaults['Next driver number'] = str(next_driver_number)
                    
        # Write updated defaults back to file
            FV.write_defaults(defaults)    
                    
        # Append the new employee's information to Employees.dat
            SN.append_employee_data(user_info, filename="Employees_test.txt")
            print(f"--- SUCCESS!! ---")
            print(f" Default settings successfully updated and saved to Defaults.dat!")
            print(f" Employee data for {user_info['driver_number']}: {user_info['first_name']} {user_info['last_name']} has been successfully saved to Employees.txt.")

            # Ask if the user wants to input another employee
            print()
            add_another = FV.prompt_and_validate(
                "Input another employee? (Y/N): ",
                "yes_no",
                "Please enter Y for YES and N for No."
                )
            
            if add_another.lower() != 'y':
                print()
                print("Returning to main menu...")
                print()
                break  # Exiting the loop to return to the main menu
        else:
            # If the user decides not to save, they're prompted to confirm starting over or returning to the main menu
            print()
            restart_or_menu = FV.prompt_and_validate(
                "Start over with a new employee entry? (Y/N): ",
                "yes_no",
                "Please enter Y to start over, or N to return to the main menu."
            )
            if restart_or_menu.lower() != 'y':
                print("\nReturning to main menu...")
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


