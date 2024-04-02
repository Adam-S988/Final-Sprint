## DESCRIPTION: Main Menu for 5 Python Programs / Sprint 1
## DATE: 03/29/2024 - 
## GROUP: Nine

import Functions as FV
import SnFunctions as SN

defaults = FV.read_defaults()


### EMPTY MAIN MENU ###
def main_menu():
    while True:
        print(f"            Main Menu             ")
        print(f"----------------------------------")
        print(f"1. Enter a New Employee (driver). ")
        print(f"2. Enter Company Revenues. ")
        print(f"3. Enter Company Expenses. ")
        print(f"4. Track Car Rentals. ")
        print(f"5. Record Employee Payment. ")
        print(f"6. Print Company Profit Listing.")
        print(f"7. Print Driver Financial Listing.")
        print(f"8. Your report - add description here.")
        print(f"9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            
            # Read default settings, specifically looking for the next available driver number
            
            next_driver_number = int(defaults['Next driver number'])

            # Collect user information through the employee functions module
            user_info = SN.collect_user_info()
            license_info = SN.collect_and_validate_drivers_license(user_info)
            
            # Update user_info with license information and the next driver number
            user_info.update(license_info)
            user_info['driver_number'] = next_driver_number
            
            # Prepare for the next employee by incrementing the driver number
            next_driver_number += 1
            defaults['Next driver number'] = str(next_driver_number)
            
            # Write updated defaults back to file
            FV.write_defaults(defaults)
            print("Default settings successfully updated and saved to Defaults.dat.")
            
            # Append the new employee's information to Employees.dat
            FV.append_employee_data(user_info, filename="Employees.dat")
            print(f"Employee data for {user_info['driver_number']}: {user_info['first_name']} {user_info['last_name']} has been successfully saved to Employees.dat.")

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
    print("placeholder1")
    print()

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


