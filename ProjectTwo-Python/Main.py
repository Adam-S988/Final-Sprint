## DESCRIPTION: Main Menu for 5 Python Programs / Sprint 1
## DATE CREATED: 03/29/2024
## GROUP: Nine

from datetime import datetime
import Functions as FV
import NewDriver as ND



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
            ND.program1(defaults)
        elif choice == '2':
            program2()
        elif choice == '3':
            program3()
        elif choice == '4':
            FV.program4()
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



### PLACEHOLDER COMPANY PROGRAMS ###

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

    defaults = FV.read_defaults()

    last_run_date_str = defaults.get('Last Run Date')
    today_str = datetime.today().strftime('%m/%d/%Y')

    if last_run_date_str:
        # Parse the last run date and today's date using MM/DD/YYYY format
        last_run_date = datetime.strptime(last_run_date_str, '%m/%d/%Y')
        today = datetime.strptime(today_str, '%m/%d/%Y')

        # Check if the current month is greater than the last run month OR
        # if the current year is greater than the last runtime's year
        # This accounts for the program not being run on the 1st, ensuring the fees are not missed.
        if today.year > last_run_date.year or (today.year == last_run_date.year and today.month > last_run_date.month):
            print("CHARGING MONTHLY FEES...")
            next_transaction_number = FV.charge_stand_fees()
            defaults['Next transaction number'] = str(next_transaction_number)
            message = "IMPORTANT NOTICE! MONTHLY STANDARD FEES HAVE BEEN APPLIED!! "
        else:
            message = "NO STANDARD FEES APPLIED TODAY. "
    else:
        message = "FIRST OPERATION OF PROGRAM DETECTED. TODAY'S DATE HAS BEEN LOGGED. "

    # Update 'Last Run Date' in defaults to todayt
    defaults['Last Run Date'] = today_str

    # Write the updated defaults back to the file
    FV.write_defaults(defaults, "Defaults.dat")    
    
    # prompt user to hit enter before continuing program
    print()
    input(f"{message}PRESS ENTER TO CONTINUE TO MAIN MENU")

    main_menu()


