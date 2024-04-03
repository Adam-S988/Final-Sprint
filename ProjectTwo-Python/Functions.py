## DESCRIPTION: Collection of useful Python functions for input/validation scenarios
## DATE CREATED: 03/30/2024
## DATE LAST MODIFIED: 004/03/2024
## GROUP NUMBER: Nine



#   |-----------|   #     
#   | LIBRARIES |   #
#   |-----------|   #


# Imports required to be added to main program for ensuring these functions work
# Not necessarily used in this version, but are being left in for possible soon-to-be implemented functions
import string
from datetime import datetime, timedelta
import re
import calendar


# Reads default.dat
def read_defaults(filename="Defaults.dat"):
    '''
    Reads key-value pairs from a defaults file and returns them as a dictionary.

    Returns:
    - dict: A dictionary containing all key-value pairs read from the file.
    '''
    defaults = {}
    try:
        # automatically handles file closing, even if exceptions occur. This method reduces the risk of leaving files open
        with open(filename, 'r') as file:
            for line in file:
                key, value = [item.strip() for item in line.split(':', 1)]
                defaults[key] = value
    except FileNotFoundError: # Error handling for file not found
        print(f"File {filename} not found.")
    return defaults


# Reads default.dat
def write_defaults(defaults, filename="Defaults.dat"):
    '''
    Writes the contents of a dictionary to the specified file as key-value pairs.

    Parameters:
    - defaults (dict): The dictionary containing key-value pairs to write to the file.
    - filename (str): The name of the file to write to. Defaults to "Defaults.dat".
    '''
    try:
        with open(filename, 'w') as file: # Using context manager for safe file handling
            # Joining dictionary items into a formatted string and writing to file
            file.write('\n'.join(f"{key}: {value}" for key, value in defaults.items()))
    except Exception as e: # Error handling for file not found
        print(f"Error writing to {filename}: {e}")


# Returns the last day of the specified month and year.
def last_day_of_month(year, month):
    """
    Returns the last day of the specified month and year.
    
    Parameters:
    - year (int): The year of the date.
    - month (int): The month of the date.
    
    Returns:
    - int: The last day of the given month and year.
    """
    # calendar.monthrange returns a tuple (weekday of first day of the month, number of days in month)
    _, last_day = calendar.monthrange(year, month)
    return last_day


# A function for streamlining the date collection process into its own "loop"
def collect_date_info():
    """
    Prompts the user to individually enter the month, day, and year of a date, and returns these components.

    Returns:
        tuple: A tuple containing the month, day, and year entered by the user.
    """
    
    month = prompt_and_validate("Enter the month (MM): ", 'month', "Please enter a valid month.")
    day = prompt_and_validate("Enter the day (DD): ", 'day', "Please enter a valid day.")
    year = prompt_and_validate("Enter the year (YYYY): ", 'year', "Please enter a valid year.")
    return month, day, year


# Joins dates together and then validates
def validate_full_date():
    """
    Continuously prompts the user to enter the components of a date until a valid date is entered.
    Validates the assembled date to ensure it's a real date (e.g., not February 30th).

    Returns:
        str: The valid date in mm/dd/yyyy format.
    """
    valid_date = False
    while not valid_date:        
        month, day, year = collect_date_info()
        try:
          # Attempt to create a datetime object with the given inputs to validate the date
            new_date = datetime(int(year), int(month), int(day))
            valid_date = True
        except ValueError:
          # If an exception is caught, it means the date is invalid
            print("The entered date is not valid. Please try again.")
  # Return the valid date in mm/dd/yyyy format
    return new_date, new_date.strftime("%m/%d/%Y")


# Helper Function #1
# Function for confirming inputs before proceeding
def get_confirmation_for_input(input_value):
    """
    Asks the user to confirm the given input value, using the Yes/No validation from is_valid_input.

    Parameters:
    - input_value (str): The input value to be confirmed.

    Returns:
    - bool: True if the input is confirmed, False otherwise.
    """


  # Prompt the user to confirm their input by entering 'Y' for Yes or 'N' for No
    confirmation_prompt = f"Confirm input '{input_value}'? (Y/N): "

  # Start a loop to repeatedly ask for confirmation if the input is invalid
    while True:
      # Get the user's confirmation input, remove leading/trailing spaces, and convert to uppercase
        confirmation = input(confirmation_prompt).strip().upper()

      # Validate the confirmation input to ensure it's either 'Y' or 'N'
        is_valid, _ = is_valid_input(confirmation, 'yes_no')

      # If the confirmation input is valid (either 'Y' or 'N')
        if is_valid:
          # Return True if the user confirmed with 'Y', indicating positive confirmation
            return confirmation == 'Y'
      # If the input is not a valid 'yes_no' response, inform the user and prompt again
        print("Invalid confirmation. Please enter 'Y' for Yes or 'N' for No.")


# Helper Function #2
# Takes Information and processes it via the is_valid_input
def prompt_and_validate(prompt_message, validation_types, error_message, initial_value=None):
    """
    Asks the user for input, checks if it's okay, and keeps asking if it's not okay. Can also check an initial piece of information first. 
    Initial values are used in situations like our Claims for QAP 4(if user enters done, itll exit. otherwise it functions((hehe)) as normal)

    Looks scary, but it can be left alone. As the programmer(you) needs to only worry about the four parameters. To see how to set up a input, refer to the get_user_info function)
    Parameters:
    - prompt_message (str): What to ask the user.
    - validation_types (list or str): The rules for checking the information.
    - error_message (str): What to say if the information doesn't follow the rules.
    - initial_value (str, optional): A first piece of information to check.
       
    Returns:
    - str: The user's information that passed the check.
    """
    

  # Validate initial value if it was provided
    if initial_value is not None:
      # Validate the initial value against the specified validation types
        is_valid, validation_message = is_valid_input(initial_value, validation_types)
        if is_valid and get_confirmation_for_input(initial_value):
          # If initial value is valid and confirmed by the user, return it immediately
            return initial_value
        else:
           # Inform the user that the initial value was not confirmed and prompt for input again
             print(f"Initial value not confirmed. Please enter the value again.")
             print()


  # Main input loop for gathering user input
    while True:
      # Prompt the user for input and strip any leading/trailing whitespace
        user_input = input(prompt_message).strip()
      # Validate the user input against the specified validation types
        is_valid, validation_message = is_valid_input(user_input, validation_types)
        if is_valid:
          # If input is valid, ask for confirmation from the user            
            if get_confirmation_for_input(user_input):
                print()
              # If the user confirms their input, return it
                return user_input
          # Handle the case where the user does not confirm their input
            print(f"Input not confirmed.")
            print()
        else:
          # If input is invalid, display the generic error message and specific validation message
            print(f"{error_message}")
            print(f"{validation_message}") # This message provides specific details on why the input was invalid(comes from is_valid_input)
            print()


# Helper Function #3
# Validates Input
# Very modular, really simply to follow the pre-existing pattern and introduce new validation types. 
# Essentially made this so id never have to make a bunch of if, else, elif statements(yucky)         
def is_valid_input(input_value, validation_types):
    """
    Checks if the given information follows certain rules, like length or character types.

    Parameters:
    - input_value (str): The information to check.
    - validation_types (list or str): The types of checks to do on the information.

    Returns:
    - tuple: A pair with a yes/no answer if the information is okay, and a message explaining why if it's not okay.
    """

    
  # Validation Sets / Constants 
  # usually taken out of function and put along top of program or in a config file 
  # which allow access throughout the entire program, and make modificaitons more convienent
    ALLOWED_NAME_CHARACTERS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.' ")
    VALID_PROVINCES = {"AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"}
    EARLIEST_YEAR = 1900  # Earliest year that will return valid    
    LATEST_YEAR = 2150    # Latest year that will return valid
    

  # Ensure validation_types is a list for consistent processing
    if isinstance(validation_types, str):
        validation_types = [validation_types]

  # Remove any leading or trailing whitespace from the input
    input_value = input_value.strip()

  # Check for non-empty input as a basic validation
    if not input_value:
        return False, "Input cannot be blank."
    
  # Iterate over each specified validation rule in the validaion types list, and apply the corresponding validation(s)
    for validation_rule in validation_types:
      # Handling dynamic validation rules by detecting the ":"
        if ':' in validation_rule:
            rule, str_value = validation_rule.split(':')
            try:

              # Min / Max Validation
                if rule in ['min_value', 'max_value']:
                    numeric_value = float(input_value)
                    limit_value = float(str_value)
                    
                  # Minimum value allowed to be entered
                    if rule == 'min_value' and numeric_value < limit_value:
                        return False, f"Value must be at least {str_value}."                    
                  # Max value allowed to be entered
                    elif rule == 'max_value' and numeric_value > limit_value:
                        return False, f"Value cannot exceed {str_value}."
                    
              # Maximum character validations    
                elif rule in ['min_character_length', 'max_character_length']:
                    limit_length = int(str_value)

                  # Minimum characters acceptable for entry
                    if rule == 'min_character_length' and len(input_value) < limit_length:
                        return False, f"Input must be at least {limit_length} characters."                    
                  # Maximum length accepted for this entry
                    elif rule == 'max_character_length' and len(input_value) > limit_length:
                        return False, f"Input exceeds the maximum allowed length of {limit_length} characters."

            except ValueError:
                return False, "Invalid value for length or range validation."                   
    

      # The 'empty' validation type is used when no validations types are needed other ensuring no blank input
        elif validation_rule == 'empty' and len(input_value) < 1:
            return False, "Data Entry Error - Input Can not be blank"  
        
      # Validate against character set for names
        elif validation_rule == 'name' and not set(input_value).issubset(ALLOWED_NAME_CHARACTERS):
            return False, "Data Entry Error - Please use only allowed characters."

      # Validate phone numbers with more flexible patterns
        elif validation_rule == 'phone_number':
            phone_pattern = r"^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$"  # Pattern example: (123) 456-7890 or 123-456-7890 or 1234567890
            if not re.match(phone_pattern, input_value):
                return False, "Data Entry Error - Please enter a valid 10-digit phone number."

      # Validate province against a set of valid abbreviations    
        elif validation_rule == 'province' and input_value.upper() not in VALID_PROVINCES:
            return False, "Data Entry Error - Please enter a valid province abbreviation."

      # Validate Canadian postal codes with an optional space
        elif validation_rule == 'postal_code':
            postal_code_pattern = r"^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$"  # Pattern example: A1A 1A1 or A1A1A1
            if not re.match(postal_code_pattern, input_value):
                return False, "Data Entry Error - Invalid postal code format."

      # Validate yes/no inputs    
        elif validation_rule == 'yes_no' and input_value.lower() not in ['y', 'n']:
            return False, "Data Entry Error - Answer Yes or No by typing Y or N."

      # Validate day  
        elif validation_rule == 'day':
            try:
                day = int(input_value)
                if not 1 <= day <= 31:
                    return False, "Data Entry Error - Please enter a value between 1 and 31."
            except ValueError:
                return False, "Data Entry Error - Please enter a numeric value."

      # Validate month    
        elif validation_rule == 'month':
            try:
                month = int(input_value)
                if not 1 <= month <= 12:
                    return False, "Data Entry Error - Please enter a value between 1 and 12."
            except ValueError:
                return False, "Data Entry Error - Please enter a numeric value."

      # Validate year within a specific range    
        elif validation_rule == 'year':
            try:
                year = int(input_value)
                if not EARLIEST_YEAR <= year <= LATEST_YEAR:
                    return False, "Data Entry Error - Please enter a value between 1900 and 2150."
            except ValueError:
                return False, "Data Entry Error - Please enter a numeric value."

      # Validate positive integers using regex to allow numbers without leading zeros
        elif validation_rule == 'positive_integer':
            positive_int_pattern = r"^[1-9]\d*$"  # Matches positive integers without leading zeros
            if not re.match(positive_int_pattern, input_value):
                return False, "Data Entry Error - Invalid input. Please enter a positive integer."
            
      # Validate positive floats with regex, allowing for decimals but not leading zeros before the decimal point unless the number is less than 1
        elif validation_rule == 'positive_float':
            positive_float_pattern = r"^(?:0\.\d+|[1-9]\d*(\.\d+)?)$"  # Matches positive floats
            if not re.match(positive_float_pattern, input_value):
                return False, "Data Entry Error - Value must be a positive float."
      
      # Validate alphanumeric inputs(ABC123) accepts dashes AND spaces (709 LOL AND  404-ERR)
        elif validation_rule == 'alphanumeric':
            if not input_value.replace('-', '').replace(' ', '').isalnum(): # Allowing dashes and spaces
                return False, "Data Entry Error - Only alphanumeric characters, dashes, and spaces are allowed."
      
      # Validate NL Drivers licencse, in a simple generic fashion
        elif validation_rule == 'NL_driver_license':
            nl_license_pattern = r"^[A-Za-z]\d{7}$"  # Hypothetical pattern for Newfoundland and Labrador
            if not re.match(nl_license_pattern, input_value):
                return False, "Data Entry Error - Invalid NL driver's license format. Expected format: A1234567."

      # Expiry Date Validation
        elif validation_rule == 'expiry_date_MMYYYY':
            try:
                exp_month, exp_year = map(int, input_value.split('/'))
                if exp_month < 1 or exp_month > 12:
                    return False, "Data Entry Error - Month must be between 01 and 12."
                expiry_date = datetime(exp_year, exp_month, last_day_of_month(exp_month, exp_year))
                if expiry_date <= datetime.now():
                    return False, "Data Entry Error - The expiry date must be in the future."
            except ValueError:
                return False, "Data Entry Error - Invalid date format. Expected MM/YYYY."


  # If all validations pass, return True with a generic success message    
    return True, "Valid input."
