## DESCRIPTION: Collection of useful Python functions for input/validation scenarios
## Date: 03/30/2024
## Group Name: Nine

#import required to be added to main program to ensure these functions work
import string


# Helper Function #1
# function for onfirming inputs before proceeding
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
    PHONE_NUMBER_LENGTH = 10
    POSTAL_CODE_LENGTH = 6
    LONG_VAR_MAX_LENGTH = 14  # Used to specifically prevent "bigger" variables from exceeding certain lengths
    SHORT_VAR_MAX_LENGTH = 5  # Used to ensure specific "smaller" variables dont exceed their own respected lengths
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

    # Iterate over each specified validation type and apply the corresponding validation
    for validation_type in validation_types:

        # The 'empty' validation type is redundant with the initial non-empty check and can be removed or adjusted.
        if validation_type == 'empty':
            if len(input_value) < 1:
                return False, "Input Can not be blank" 

        # Validate against a maximum length for 'long' type inputs    
        elif validation_type == 'long':
            if len(input_value) > LONG_VAR_MAX_LENGTH:
                return False, "Input exceeds the maximum allowed length of 10 characters."

        # Validate against a maximum length for 'short' type inputs    
        elif validation_type == 'short':
            if len(input_value) > SHORT_VAR_MAX_LENGTH :
                return False, "Input exceeds the maximum allowed length of 5 characters."
        
        # Validate against character set for names
        elif validation_type == 'name':
            if not set(input_value).issubset(ALLOWED_NAME_CHARACTERS):
                return False, "Invalid name. Please use only allowed characters."

        # Validate phone numbers for digit count and ensuring if it is a numeric value    
        elif validation_type == 'phone_number':
            if not (len(input_value) == PHONE_NUMBER_LENGTH and input_value.isdigit()):
                return False, "Invalid phone number. Please enter a 10-digit numeric phone number."

        # Validate province against a set of valid abbreviations    
        elif validation_type == 'province':
            if input_value.upper() not in VALID_PROVINCES:
                return False, "Invalid province. Please enter a valid abbreviation."

        # Validate postal codes for length and specific format    
        elif validation_type == 'postal_code':
            if not (len(input_value) == POSTAL_CODE_LENGTH and input_value[0].isalpha() and input_value[1].isdigit()):
                return False, "Invalid postal code format."

        # Validate yes/no inputs    
        elif validation_type == 'yes_no':
            if input_value.lower() not in ['y', 'n']:
                return False, "Data Entry Error - Answer Yes or No by typing Y or N."

        # Validate day of the month    
        elif validation_type == 'day':
            try:
                day = int(input_value)
                if not 1 <= day <= 31:
                    return False, "Invalid day. Please enter a value between 1 and 31."
            except ValueError:
                return False, "Invalid day. Please enter a numeric value."

        # Validate month    
        elif validation_type == 'month':
            try:
                month = int(input_value)
                if not 1 <= month <= 12:
                    return False, "Invalid month. Please enter a value between 1 and 12."
            except ValueError:
                return False, "Invalid month. Please enter a numeric value."

        # Validate year within a specific range    
        elif validation_type == 'year':
            try:
                year = int(input_value)
                if not EARLIEST_YEAR <= year <= LATEST_YEAR:
                    return False, "Invalid year. Please enter a value between 1900 and 2150."
            except ValueError:
                return False, "Invalid year. Please enter a numeric value."

        # Validate positive integers    
        elif validation_type == 'positive_integer':
            if not (input_value.isdigit() and int(input_value) > 0):
                return False, "Invalid input. Please enter a positive integer."
            
        # Validate positive floating-point numbers    
        elif validation_type == 'positive_float':
            try:
                value = float(input_value)
                if value <= 0:
                    return False, "Value must be a positive float."
            except ValueError:
                return False, "Invalid input. Please enter a valid floating-point number."
            
    # If all validations pass, return True with a generic success message    
    return True, "Valid input."


# This is to just provide an example of how to use the "helper" functions
# This function can be renamed/repurposed for any input collection scenario)
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
    "error message here" --------> This is a secondary error message. The validation function will return the error based upon the validation type, so i recommend using the section for suggisting/listing correct inputs.
    )   

    Returns:
        A dictionary with all the user's information that's been checked and fixed up to look nice.
    """


    # Collect and validate the first name
    first_name = prompt_and_validate(
        "Enter the first name: ", 
        ['name', 'long'],  
        "Please enter a valid first name"
    ).title()

    # Collect and validate the last name similar to the first name
    last_name = prompt_and_validate(
        "Enter the last name: ", 
        ['name', 'long'],  
        "Please use only allowed characters."
    ).title()

    # Collect and validate to only ensure address input is not empty
    address = prompt_and_validate(
        "Enter the street address: ", 
        'empty',  
        "Please enter a valid street address."
    )
    
    # Collect and validate the city name, ensuring it's contains valid naming characters, and isnt empty(empty validation isnt necessary to prevent input, it just helps provide more accurate error message if user enters blank inputs)
    city = string.capwords(prompt_and_validate(
        "Enter the city: ", 
        ['name', 'empty'],  
        "Please use only allowed characters for the city name."
    ))

    # Collect and validate the province abbreviations ensuring it's one of the defined valid provinces
    province = prompt_and_validate(
        "Enter the province (abbreviation): ", 
        ['province', 'empty'],
        "Please enter a valid province abbreviation(NL, QC, ON)"
    ).upper()

    # Collect and validate the postal code ensuring it follows a specific format and is not empty
    postal_code = prompt_and_validate(
        "Please enter the postal code (Format: A1A1A1): ", 
        ['postal_code', 'empty'],
        "Please enter a valid postal code in the format X1X1X1 without spaces."
    ).upper().replace(" ", "")

    # Collect and validate the phone number ensuring it's numeric and EXACTLY 10 digits long
    phone_number = prompt_and_validate(
        "Enter customer's phone number (10 digits): ", 
        ['phone_number', 'empty'],
        "Please enter a valid 10-digit numeric phone number without any spaces or special characters."
    )

    # Compile all collected and validated inputs into a dictionary for easy access, storage, and manipulation
    return {
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'province': province,
        'postal_code': postal_code,
        'phone_number': phone_number,
    }

