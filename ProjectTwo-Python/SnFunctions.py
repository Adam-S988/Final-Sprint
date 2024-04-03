## DESCRIPTION: Functions for colleting/handling the new employee(driver). Collection of python functions delegated to its own module.
## DATE CREATED: 04/02/2024
## DATE LAST MODIFIED: 004/03/2024
## GROUP NUMBER: Nine




#imports required to be added to main program for ensuring these functions work
import string
from datetime import datetime, timedelta
import re
import Functions as FV

# This function can be renamed/repurposed for any input collection scenario
def collect_user_info():
    """
    This function asks the user a bunch of questions to get their information. Like their name, address, etc. 
    For each question, it makes sure the answer makes sense (like making sure a name doesn't have numbers in it).
    If the answer is good, it might change how it looks (like making sure all the letters in a name are the right case) and remembers it. 
    Once it has all the answers, it puts them into a dictionary so we can use them later.
    This function is highly customizable, being able to be adjusted to any type of "input" scenario, with as many inputs as needed.

    
    This is just an example of how the previous two functions work. To add a new variable it just follows the format:
    
    variableName = prompt_and_validate(
    "prompt here" ---------------> replaces the input() stuff
    ['validationType, etc'] -----> This is a list, in which you enter what types of validations you want to use(ie name, address, etc)
    "error message here" --------> This is a secondary error message. The validation function will return the error based upon the validation type, so I recommend using this section for suggesting/listing correct inputs.
    )   

    Returns:
        A dictionary with all the user's information that's been checked and fixed up to look nice.
    """


  # Collect and validate the first name
    first_name = FV.prompt_and_validate(
        "Enter the first name: ", 
        ['name', 'max_character_length:20'],  
        "Please enter a valid first name"
        ).title()

  # Collect and validate the last name similar to the first name
    last_name = FV.prompt_and_validate(
        "Enter the last name: ", 
        ['name', 'max_character_length:20'],  
        "Please use only allowed characters."
        ).title()

  # Collect and validate to only ensure address input is not empty
    address = FV.prompt_and_validate(
        "Enter the street address: ", 
        'empty',  
        "Please enter a valid street address."
        )
    
  # Collect and validate the city name, ensuring it's contains valid naming characters, and isnt empty(empty validation isnt necessary to prevent input, it just helps provide more accurate error message if user enters blank inputs)
    city = string.capwords(FV.prompt_and_validate(
        "Enter the city: ", 
        ['name',],  
        "Please use only allowed characters for the city name."
        ))

  # Collect and validate the province abbreviations ensuring it's one of the defined valid provinces
    province = FV.prompt_and_validate(
        "Enter the province (abbreviation): ", 
        ['province',],
        "Please enter a valid province abbreviation(NL, QC, ON)"
        ).upper()

  # Collect and validate the postal code ensuring it follows a specific format and is not empty
    postal_code = FV.prompt_and_validate(
        "Please enter the postal code (Formats: A1A 1A1 or A1A1A1): ", 
        ['postal_code',],
        "Please enter a valid postal code in the format A1A 1A1 or A1A1A1."
        ).upper().replace(" ", "")

  # Collect and validate the phone number ensuring it's numeric and EXACTLY 10 digits long
    phone_number = FV.prompt_and_validate(
        "Enter customer's phone number (10 digits): ", 
        ['phone_number',],
        "Please enter a valid 10-digit numeric phone number .Formats like 1234567890, 123-456-7890, or (123) 456-7890 are accepted."
        ).replace(" ", "")

    insurance_company = string.capwords(FV.prompt_and_validate(
        "Enter the insurance policy company name: ", 
        ['name', 'min_character_length:2', 'max_character_length:20'],  
        "Please enter a valid company name (2-20 characters)."
        ))
    
    insurance_policy_number = FV.prompt_and_validate(
        "Enter the insurance policy number: ", 
        ['alphanumeric', 'min_character_length:5', 'max_character_length:20'],  
        "Please enter a valid policy number (5-20 characters, alphanumeric)."
        ).upper()
    
    owns_car = FV.prompt_and_validate(
        "Will you be using your own vehicle?(Enter Y/N for Yes/No): ",
        ['yes_no',],
        "Please enter Y for yes, or N for no."
        ).upper()

  # CALCULATED FIELD: Collects day, month, year, and assembles/validates as a full date, then calculates the age based on today's date.
    print("Please enter the employee date of birth.")
    date_of_birth_datetime, date_of_birth = FV.validate_full_date()
    today = datetime.today()
    age = today.year - date_of_birth_datetime.year - ((today.month, today.day) < (date_of_birth_datetime.month, date_of_birth_datetime.day))
    age = str(age)

  # Compile all collected and validated inputs into a dictionary for easy access, storage, and manipulation
    return {
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'province': province,
        'postal_code': postal_code,
        'phone_number': phone_number,
        'date_of_birth': date_of_birth,
        'age':age,
        'insurance_company':insurance_company,
        'insurance_policy_number':insurance_policy_number,
        'owns_car':owns_car
        }


# Continuously prompts for and validates a driver's license and its expiry date.
def collect_and_validate_drivers_license(user_info):
    """
    Continuously prompts for and validates a driver's license and its expiry date.
    
    Parameters:
    - user_info (dict): Dictionary containing at least 'first_name' and 'last_name'.
    
    Returns:
    - dict: A dictionary with valid 'drivers_license' and 'expiry_date' entries.
    """

    
    # Construct the expected initials for the driver's license validation
    initials = user_info['first_name'][0].upper() + user_info['last_name'][0].upper()

    while True:
        drivers_license = input(f"Enter your 7-digit driver's license number (starting with your initials {initials}): ").upper().strip()
        # Newfoundland and Labrador driver's license pattern: 2 letters followed by 7 digits
        nl_license_pattern = f"^{initials}\\d{{7}}$"

        # Validate driver's license format (initials followed by 7 digits)        
        if re.match(nl_license_pattern, drivers_license):
            break  # Exit the loop if the driver's license is valid
        print(f"Invalid driver's license format(Expected format: {initials}1234567):   ")

    # Separate loop for expiry date validation
    while True:
        expiry_date_input = input("Enter the expiry date (MM/YYYY): ")

        try:
            exp_month, exp_year = map(int, expiry_date_input.split('/'))
            expiry_date = datetime(exp_year, exp_month, FV.last_day_of_month(exp_year, exp_month))
            if expiry_date <= datetime.now():
                raise ValueError("The expiry date must be in the future.")
            break  # Exit the loop if the expiry date is valid
        except (ValueError, IndexError):
            print("Invalid expiry date format or date is not in the future. Please enter in MM/YYYY format.")

    # If both inputs are valid, compile and return the results
    return {'drivers_license': drivers_license, 'expiry_date': expiry_date.strftime("%m/%Y")}


# sends employee data to Employees.dat
def append_employee_data(employee_data, filename="Employees_test.txt"):
    try:
        with open(filename, 'a') as file: # Using context manager for safe file handling
            # Converting dictionary values to a string and appending to file
            employee_str = ', '.join(str(value) for value in employee_data.values())
            file.write(f"{employee_str}\n")
    except Exception as e:
        print(f"Error appending to {filename}: {e}")



'''
#debugging code stored here

import os

# Debug: Print the current working directory
print(f"Current Working Directory: {os.getcwd()}")

# Debug: Check if the file exists
filename = "Defaults.dat"
filepath = os.path.join(os.getcwd(), filename)
if os.path.isfile(filepath):
    print(f"Found file at {filepath}")
else:
    print(f"File not found at {filepath}")


def read_defaults(filename="Defaults.dat"):
    defaults = {}
    try:
        with open(filename, "r") as f:  # Use "r" for read mode
            for line in f:
                if ": " in line:  # Check for the delimiter
                    key, value = line.split(": ", 1)  # Split each line at the delimiter
                    defaults[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
    return defaults


defaults = read_defaults()

# debug print/test
# Reading defaults and initializing next driver number
defaults = FV.read_defaults()
next_driver_number = int(defaults['Next driver number'])

# Collecting user and license information
user_info = collect_user_info()
license_info = collect_and_validate_drivers_license(user_info)
user_info.update(license_info)

# Correctly adding next_driver_number to user_info
user_info['driver_number'] = next_driver_number

# Increment next driver number for future use
next_driver_number += 1

# Updating defaults with the new next driver number
defaults['Next driver number'] = str(next_driver_number)

# Writing the updated defaults back to Defaults.dat
FV.write_defaults(defaults)
print("Default settings successfully updated and saved to Defaults.dat.")

# Append the user_info to Employees.dat
append_employee_data(user_info, filename="Employees.dat")
print(f"Employee data for{user_info['driver_number']}: {user_info['first_name']} {user_info['last_name']} has been successfully saved to Employees.dat.")
# Debug print/test to display user_info
print(user_info)
for key, value in user_info.items():
    print(f"   | {key:>22s} -- {value:<33s}|")


    
'''