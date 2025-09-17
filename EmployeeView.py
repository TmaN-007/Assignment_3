"""
Employee Management System - View Module

This module handles all user interface operations including:
- Menu display
- User input prompting
- Employee data display
- User message display

The view layer contains no business logic - only input/output operations.
"""


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nEmployee Management System")
    print("1. Create New Employee")
    print("2. Edit Existing Employee")
    print("3. Delete Existing Employee")
    print("4. Display Employees")
    print("5. Quit")
    print('\n')


def get_user_input(prompt, input_type="string", validation_func=None):
    """
    Prompt user for input with optional type conversion and validation.

    Args:
        prompt (str): The prompt message to display
        input_type (str): Type of input expected ("string", "int", "float")
        validation_func (function, optional): Function to validate input

    Returns:
        The user input converted to the specified type

    Raises:
        ValueError: If input cannot be converted to specified type
    """
    while True:
        try:
            user_input = input(prompt).strip()

            # Handle empty input
            if not user_input:
                if input_type == "string":
                    return user_input
                else:
                    print("Input cannot be empty. Please try again.")
                    continue

            # Convert to specified type
            if input_type == "int":
                converted_input = int(user_input)
            elif input_type == "float":
                converted_input = float(user_input)
            else:
                converted_input = user_input

            # Apply validation function if provided
            if validation_func:
                if validation_func(converted_input):
                    return converted_input
                else:
                    print("Invalid input. Please try again.")
                    continue

            return converted_input

        except ValueError:
            print(f"Invalid input type. Expected {input_type}. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return None


def get_employee_data(is_manager=False):
    """
    Prompt user for employee data input.

    Args:
        is_manager (bool): Whether to collect manager-specific data

    Returns:
        dict: Dictionary containing employee data
    """
    print(f"\nEnter {'Manager' if is_manager else 'Employee'} Information:")
    print("-" * 40)

    data = {}
    data['id'] = get_user_input("Employee ID: ", "string")
    if data['id'] is None:
        return None

    data['fname'] = get_user_input("First Name: ", "string")
    if data['fname'] is None:
        return None

    data['lname'] = get_user_input("Last Name: ", "string")
    if data['lname'] is None:
        return None

    data['department'] = get_user_input("Department (3 uppercase letters): ", "string")
    if data['department'] is None:
        return None

    data['ph_number'] = get_user_input("Phone Number (any format): ", "string")
    if data['ph_number'] is None:
        return None

    if is_manager:
        data['team_size'] = get_user_input("Team Size: ", "int")
        if data['team_size'] is None:
            return None

        data['office_number'] = get_user_input("Office Number: ", "string")
        if data['office_number'] is None:
            return None

    return data


def display_employees(employees, title="Employee List"):
    """
    Display employees in a clean, formatted table.

    Args:
        employees (list): List of Employee/Manager objects to display
        title (str): Title to display above the list
    """
    if not employees:
        show_message("No employees found.", "info")
        return

    print(f"\n{title}")
    print("="*100)
    print(f"{'#':<3} {'ID':<8} {'Name':<25} {'Dept':<6} {'Phone':<15} {'Type':<10} {'Details':<20}")
    print("-"*100)

    for i, emp in enumerate(employees, 1):
        emp_type = type(emp).__name__
        details = ""

        # Add manager-specific details
        if emp_type == "Manager":
            details = f"Team:{emp.team_size}, Office:{emp.office_number}"

        print(f"{i:<3} {emp.id:<8} {emp.fname + ' ' + emp.lname:<25} {emp.department:<6} "
              f"{emp.ph_number:<15} {emp_type:<10} {details:<20}")

    print("-"*100)
    print(f"Total: {len(employees)} employees")


def display_employee_details(employee, index=None):
    """
    Display detailed information for a single employee.

    Args:
        employee: Employee or Manager object
        index (int, optional): Index number to display
    """
    emp_type = type(employee).__name__

    print(f"\n{emp_type} Details" + (f" (Index: {index})" if index is not None else ""))
    print("-" * 40)
    print(f"ID: {employee.id}")
    print(f"Name: {employee.fname} {employee.lname}")
    print(f"Department: {employee.department}")
    print(f"Phone (Formatted): {employee.ph_number}")
    print(f"Phone (Unformatted): {employee.getphNumber()}")

    if emp_type == "Manager":
        print(f"Team Size: {employee.team_size}")
        print(f"Office: {employee.office_number}")


def show_message(message, msg_type="info"):
    """
    Display a message to the user with appropriate formatting.

    Args:
        message (str): The message to display
        msg_type (str): Type of message ("info", "success", "error", "warning")
    """
    symbols = {
        "info": "ℹ",
        "success": "✓",
        "error": "✗",
        "warning": "⚠"
    }

    symbol = symbols.get(msg_type, "•")
    print(f"\n{symbol} {message}")


def confirm_action(action_description):
    """
    Ask user to confirm an action.

    Args:
        action_description (str): Description of the action to confirm

    Returns:
        bool: True if user confirms, False otherwise
    """
    while True:
        response = get_user_input(f"Are you sure you want to {action_description}? (y/n): ", "string")
        if response is None:
            return False

        response = response.lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")


def get_menu_choice():
    """
    Get and validate menu choice from user.

    Returns:
        int: Valid menu choice (1-8) or None if cancelled
    """
    def validate_choice(choice):
        return 1 <= choice <= 5

    return get_user_input("Select an option (1-5): ", "int", validate_choice)


def get_employee_index(max_index):
    """
    Get and validate employee index from user.

    Args:
        max_index (int): Maximum valid index

    Returns:
        int: Valid employee index (0-based) or None if cancelled
    """
    def validate_index(index):
        return 0 <= index < max_index

    choice = get_user_input(f"Enter employee number (1-{max_index}): ", "int")
    if choice is None:
        return None

    # Convert from 1-based to 0-based indexing
    index = choice - 1
    if validate_index(index):
        return index
    else:
        show_message(f"Invalid employee number. Must be between 1 and {max_index}.", "error")
        return None


def get_filename():
    """
    Get filename from user with default option.

    Returns:
        str: Filename to use
    """
    filename = get_user_input("Enter filename (press Enter for 'employee_data.csv'): ", "string")
    if filename is None:
        return None
    return filename if filename else "employee_data.csv"


def pause_for_user():
    """
    Pause execution and wait for user to press Enter.
    """
    input("\nPress Enter to continue...")


def clear_screen():
    """
    Clear the screen (works on most terminals).
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')