## DESCRIPTION: Functions for colleting/handling the new employee(driver). Collection of python functions delegated to its own module.
## DATE CREATED: 04/02/2024
## DATE LAST MODIFIED: 04/05/2024
## GROUP NUMBER: Nine




#imports required to be added to main program for ensuring these functions work
import string
from datetime import datetime, timedelta
import re
import Functions as FV

# This function can be renamed/repurposed for any input collection scenario
def collect_user_info(driver_number):
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

    user_info = {'driver_number': driver_number}

  # Collect and validate the first name
    first_name = FV.prompt_and_validate(
        "ENTER THE EMPLOYEE NAME: ", 
        ['name', 'max_character_length:20'],  
        "PLEASE ENTER A NAME NO LARGER THAN 20 CHARACTERS"
        ).title()

  # Collect and validate the last name similar to the first name
    last_name = FV.prompt_and_validate(
        "ENTER THE EMPLOYEE LAST NAME: ", 
        ['name', 'max_character_length:20'],  
        "PLEASE ENTER A LAST NAME NO LARGER THAN 20 CHARACTERS"
        ).title()

  # Collect and validate to only ensure address input is not empty
    address = string.capwords(FV.prompt_and_validate(
        "ENTER THE EMPLOYEES HOUSE NUMBER AND STREET ADDRESS: ", 
        ['empty', 'max_character_length:30'],  
        "PLEASE ENTER A VALID ADDRESS"
        ))
    
  # Collect and validate the city name, ensuring it's contains valid naming characters, and isnt empty(empty validation isnt necessary to prevent input, it just helps provide more accurate error message if user enters blank inputs)
    city = string.capwords(FV.prompt_and_validate(
        "ENTER THE EMPLOYEE'S HOME CITY: ", 
        ['name',],  
        "PLEASE ENTER A VALID CITY NAME"
        ))

  # Collect and validate the province abbreviations ensuring it's one of the defined valid provinces
    province = FV.prompt_and_validate(
        "ENTER THE EMPLOYEE'S HOME PROVINCE (ABBREVIATION): ", 
        ['province',],
        "PLEASE ENTER A VALID ABBREVIATION(NL, QC, ON)"
        ).upper()

  # Collect and validate the postal code ensuring it follows a specific format and is not empty
    postal_code = FV.prompt_and_validate(
        "PLEASE ENTER THE EMPLOYEE HOME POSTAL CODE (Formats: A1A 1A1 or A1A1A1): ", 
        ['postal_code',],
        "PLEASE ENTER A VALID POSTAL CODE. SUCH AS A1A 1A1 or A1A1A1."
        ).upper().replace(" ", "")

  # Collect and validate the phone number ensuring it's numeric and EXACTLY 10 digits long
    phone_number = FV.prompt_and_validate(
        "ENTER THE EMPLOYEE PHONE NUMBER (10 digits): ", 
        ['phone_number',],
        "PLEASE ENTER A VALID 10-DIGIT NUMERIC PHONE NUMBER. ACCEPTED FORMATS: 1234567890, 123-456-7890, or (123) 456-7890"
        ).replace(" ", "")
    
  # Collect and validate insurance company name  
    insurance_company = (FV.prompt_and_validate(
        "ENTER NAME OF THE EMPLOYEE'S INSURANCE POLICY COMPANY: ", 
        ['name', 'min_character_length:2', 'max_character_length:20'],  
        "PLEASE ENTER A VALID COMPANY NAME (2-20 characters)."
        ))
    
  # Collect and validate insurance number, expecting 3 letters and 3-6 digits  
    insurance_policy_number = FV.prompt_and_validate(
        "ENTER THE EMPLOYEE's INSURANCE POLICY NUMBER(ABC001, ABC123456): ", 
        ['alphanumeric', 'min_character_length:6', 'max_character_length:9'],  
        "PLEASE ENTER A VALID INSURANCE POLICY NUMBER (6-9 characters, alphanumeric)."
        ).upper()
    
  # Asks if user owns their own vehicle, or if they do not.
    owns_car = FV.prompt_and_validate(
        "WILL THE EMPLOYEE BE USING THEIR OWN VEHICLE?(Enter Y/N for Yes/No): ",
        ['yes_no',],
        "PLEASE ENTER Y TO INDICATE YES. ENTER N TO INDICATE NO."
        ).upper()

  # CALCULATED FIELDS: Collects day, month, year, and assembles/validates as a full date of birth, then calculates the age based on today's date.
    print("PLEASE ENTER THE EMPLOYEE DATE OF BIRTH")
    date_of_birth_datetime, date_of_birth = FV.validate_full_date()
    today = datetime.today()
    age = today.year - date_of_birth_datetime.year - ((today.month, today.day) < (date_of_birth_datetime.month, date_of_birth_datetime.day))
    age = str(age)

  # Compile all collected and validated inputs into a dictionary for easy access, storage, and manipulation
    user_info.update({
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'province': province,
        'postal_code': postal_code,
        'phone_number': phone_number,
        'date_of_birth': date_of_birth,
        'age': age,
        'insurance_company': insurance_company,
        'insurance_policy_number': insurance_policy_number,
        'owns_car': owns_car
        })

    return user_info


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
        drivers_license = input(f"Enter the Emnployee's 7-digit driver's license number (starting with initials {initials}): ").upper().strip()
        # Newfoundland and Labrador driver's license pattern: 2 letters followed by 7 digits ( I probably shouldnt make them type their own intials... but it is what it is now.)
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
                raise ValueError("The expiry date must be in the future.(IE 2025 and beyond)") # in a real life scenario "2025" would be a variable that check the next year
            break  # Exit the loop if the expiry date is valid
        except (ValueError, IndexError):
            print("Invalid expiry date format or date is not in the future. Please enter in MM/YYYY format.")

    # If both inputs are valid, compile and return the results
    return {'drivers_license': drivers_license, 'expiry_date': expiry_date.strftime("%m/%Y")}


# Sends employee data to Employees.dat
def append_employee_data(employee_data, filename="Employees_test.txt"):
    try:
        with open(filename, 'a') as file: # Using context manager for safe file handling
            # Converting dictionary values to a string and appending to file(just incase)
            employee_str = ', '.join(str(value) for value in employee_data.values())
            file.write(f"{employee_str}\n") # my hate for newline is superseded by my hate for data files. pls no judge.
    except Exception as e:
        print(f"Error appending to {filename}: {e}")
