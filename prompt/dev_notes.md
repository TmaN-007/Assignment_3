Prompt: Write a Python class called Employee with attributes: id, fname, lname, department, and phNumber. Use private variables and getters/setters. Add validation: 
- First/last names cannot be empty or contain digits
- Department must be exactly 3 uppercase letters
- Phone number must be 10 digits
Include docstrings.

AI Suggestion: 
class Employee:
    """
    Employee class to manage employee information with validation.
    
    Attributes:
        _id (int): Employee ID
        _fname (str): First name (cannot be empty or contain digits)
        _lname (str): Last name (cannot be empty or contain digits)
        _department (str): Department code (exactly 3 uppercase letters)
        _ph_number (str): Phone number (exactly 10 digits)
    """
    
    def __init__(self, id, fname, lname, department, ph_number):
        """
        Initialize Employee object with validation.
        
        Args:
            id (int): Employee ID
            fname (str): First name
            lname (str): Last name
            department (str): Department code
            ph_number (str): Phone number
        
        Raises:
            ValueError: If any validation fails
        """
        self._id = id
        self.fname = fname
        self.lname = lname
        self.department = department
        self.ph_number = ph_number
    
    @property
    def id(self):
        """Get employee ID."""
        return self._id
    
    @id.setter
    def id(self, value):
        """Set employee ID."""
        self._id = value
    
    @property
    def fname(self):
        """Get first name."""
        return self._fname
    
    @fname.setter
    def fname(self, value):
        """
        Set first name with validation.
        
        Args:
            value (str): First name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("First name cannot contain digits")
        self._fname = value
    
    @property
    def lname(self):
        """Get last name."""
        return self._lname
    
    @lname.setter
    def lname(self, value):
        """
        Set last name with validation.
        
        Args:
            value (str): Last name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("Last name cannot contain digits")
        self._lname = value
    
    @property
    def department(self):
        """Get department code."""
        return self._department
    
    @department.setter
    def department(self, value):
        """
        Set department code with validation.
        
        Args:
            value (str): Department code
        
        Raises:
            ValueError: If department is not exactly 3 uppercase letters
        """
        if not value or len(value) != 3:
            raise ValueError("Department must be exactly 3 characters")
        if not value.isupper():
            raise ValueError("Department must be uppercase letters")
        if not value.isalpha():
            raise ValueError("Department must contain only letters")
        self._department = value
    
    @property
    def ph_number(self):
        """Get phone number."""
        return self._ph_number
    
    @ph_number.setter
    def ph_number(self, value):
        """
        Set phone number with validation.
        
        Args:
            value (str): Phone number
        
        Raises:
            ValueError: If phone number is not exactly 10 digits
        """
        if not value or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 characters")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self._ph_number = value
    
    def __str__(self):
        """Return string representation of Employee."""
        return f"Employee(ID: {self._id}, Name: {self._fname} {self._lname}, Dept: {self._department}, Phone: {self._ph_number})"
    
    def __repr__(self):
        """Return detailed string representation of Employee."""
        return f"Employee({self._id}, '{self._fname}', '{self._lname}', '{self._department}', '{self._ph_number}')"

Reflection: Copilot Generated the full class and I didn't have to fix anything


Prompt2: Update the Employee class so the employee ID is read-only after creation. Format phone numbers as (XXX)XXX-XXXX when accessed.

AI Suggestion: 
class Employee:
    """
    Employee class to manage employee information with validation.
    
    Attributes:
        _id (int): Employee ID
        _fname (str): First name (cannot be empty or contain digits)
        _lname (str): Last name (cannot be empty or contain digits)
        _department (str): Department code (exactly 3 uppercase letters)
        _ph_number (str): Phone number (exactly 10 digits)
    """
    
    def __init__(self, id, fname, lname, department, ph_number):
        """
        Initialize Employee object with validation.
        
        Args:
            id (int): Employee ID (read-only after creation)
            fname (str): First name
            lname (str): Last name
            department (str): Department code
            ph_number (str): Phone number
        
        Raises:
            ValueError: If any validation fails
        """
        self._id = id
        self._id_set = True
        self.fname = fname
        self.lname = lname
        self.department = department
        self.ph_number = ph_number
    
    @property
    def id(self):
        """Get employee ID (read-only)."""
        return self._id
    
    @property
    def fname(self):
        """Get first name."""
        return self._fname
    
    @fname.setter
    def fname(self, value):
        """
        Set first name with validation.
        
        Args:
            value (str): First name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("First name cannot contain digits")
        self._fname = value
    
    @property
    def lname(self):
        """Get last name."""
        return self._lname
    
    @lname.setter
    def lname(self, value):
        """
        Set last name with validation.
        
        Args:
            value (str): Last name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("Last name cannot contain digits")
        self._lname = value
    
    @property
    def department(self):
        """Get department code."""
        return self._department
    
    @department.setter
    def department(self, value):
        """
        Set department code with validation.
        
        Args:
            value (str): Department code
        
        Raises:
            ValueError: If department is not exactly 3 uppercase letters
        """
        if not value or len(value) != 3:
            raise ValueError("Department must be exactly 3 characters")
        if not value.isupper():
            raise ValueError("Department must be uppercase letters")
        if not value.isalpha():
            raise ValueError("Department must contain only letters")
        self._department = value
    
    @property
    def ph_number(self):
        """Get formatted phone number as (XXX)XXX-XXXX."""
        return f"({self._ph_number[:3]}){self._ph_number[3:6]}-{self._ph_number[6:]}"
    
    @ph_number.setter
    def ph_number(self, value):
        """
        Set phone number with validation.
        
        Args:
            value (str): Phone number
        
        Raises:
            ValueError: If phone number is not exactly 10 digits
        """
        if not value or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 characters")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self._ph_number = value
    
    def __str__(self):
        """Return string representation of Employee."""
        return f"Employee(ID: {self._id}, Name: {self._fname} {self._lname}, Dept: {self._department}, Phone: {self.ph_number})"
    
    def __repr__(self):
        """Return detailed string representation of Employee."""
        return f"Employee({self._id}, '{self._fname}', '{self._lname}', '{self._department}', '{self._ph_number}')"
    
    Reflection: Copilot made the id property read only in a basic sense. But the private field can still be changed directly and it added an unused flag. 

    Prompt: the id property is read only in a basic sense. But the private field can still be changed directly and it added an unused flag.

    AI Sugeestion: 
    class Employee:
    """
    Employee class to manage employee information with validation.
    
    Attributes:
        _id (int): Employee ID
        _fname (str): First name (cannot be empty or contain digits)
        _lname (str): Last name (cannot be empty or contain digits)
        _department (str): Department code (exactly 3 uppercase letters)
        _ph_number (str): Phone number (exactly 10 digits)
    """
    
    def __init__(self, id, fname, lname, department, ph_number):
        """
        Initialize Employee object with validation.
        
        Args:
            id (int): Employee ID (read-only after creation)
            fname (str): First name
            lname (str): Last name
            department (str): Department code
            ph_number (str): Phone number
        
        Raises:
            ValueError: If any validation fails
        """
        object.__setattr__(self, '_id', id)
        self.fname = fname
        self.lname = lname
        self.department = department
        self.ph_number = ph_number
    
    @property
    def id(self):
        """Get employee ID (read-only)."""
        return self._id
    
    @property
    def fname(self):
        """Get first name."""
        return self._fname
    
    @fname.setter
    def fname(self, value):
        """
        Set first name with validation.
        
        Args:
            value (str): First name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("First name cannot contain digits")
        self._fname = value
    
    @property
    def lname(self):
        """Get last name."""
        return self._lname
    
    @lname.setter
    def lname(self, value):
        """
        Set last name with validation.
        
        Args:
            value (str): Last name
        
        Raises:
            ValueError: If name is empty or contains digits
        """
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        if any(char.isdigit() for char in value):
            raise ValueError("Last name cannot contain digits")
        self._lname = value
    
    @property
    def department(self):
        """Get department code."""
        return self._department
    
    @department.setter
    def department(self, value):
        """
        Set department code with validation.
        
        Args:
            value (str): Department code
        
        Raises:
            ValueError: If department is not exactly 3 uppercase letters
        """
        if not value or len(value) != 3:
            raise ValueError("Department must be exactly 3 characters")
        if not value.isupper():
            raise ValueError("Department must be uppercase letters")
        if not value.isalpha():
            raise ValueError("Department must contain only letters")
        self._department = value
    
    @property
    def ph_number(self):
        """Get formatted phone number as (XXX)XXX-XXXX."""
        return f"({self._ph_number[:3]}){self._ph_number[3:6]}-{self._ph_number[6:]}"
    
    @ph_number.setter
    def ph_number(self, value):
        """
        Set phone number with validation.
        
        Args:
            value (str): Phone number
        
        Raises:
            ValueError: If phone number is not exactly 10 digits
        """
        if not value or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 characters")
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        self._ph_number = value
    
    def __str__(self):
        """Return string representation of Employee."""
        return f"Employee(ID: {self._id}, Name: {self._fname} {self._lname}, Dept: {self._department}, Phone: {self.ph_number})"
    
    def __repr__(self):
        """Return detailed string representation of Employee."""
        return f"Employee({self._id}, '{self._fname}', '{self._lname}', '{self._department}', '{self._ph_number}')"
    
    def __setattr__(self, name, value):
        """Prevent modification of _id after initialization."""
        if name == '_id' and hasattr(self, '_id'):
            raise AttributeError("Employee ID is read-only and cannot be modified")
        super().__setattr__(name, value)

Reflection: This time Copilot made it right.


Prompt3: Write Python functions to load and save a list of Employee objects from a CSV file called employee_data.csv. The CSV columns should be id, fname, lname, department, phNumber.

AI Suggestion:
import csv
from employee import Employee


def load_employees_from_csv(filename="employee_data.csv"):
    """
    Load Employee objects from a CSV file.
    
    Args:
        filename (str): Name of the CSV file to load from
        
    Returns:
        list: List of Employee objects
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If employee data is invalid
    """
    employees = []
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                employee = Employee(
                    id=int(row['id']),
                    fname=row['fname'],
                    lname=row['lname'],
                    department=row['department'],
                    ph_number=row['phNumber']
                )
                employees.append(employee)
                
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{filename}' not found")
    except KeyError as e:
        raise ValueError(f"Missing required column in CSV: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid employee data in CSV: {e}")
        
    return employees


def save_employees_to_csv(employees, filename="employee_data.csv"):
    """
    Save Employee objects to a CSV file.
    
    Args:
        employees (list): List of Employee objects to save
        filename (str): Name of the CSV file to save to
        
    Raises:
        IOError: If unable to write to the file
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'fname', 'lname', 'department', 'phNumber']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for employee in employees:
                writer.writerow({
                    'id': employee.id,
                    'fname': employee.fname,
                    'lname': employee.lname,
                    'department': employee.department,
                    'phNumber': employee._ph_number  # Use raw digits for storage
                })
                
    except IOError as e:
        raise IOError(f"Unable to write to CSV file '{filename}': {e}")

Reflection: Copilot did remember to call Employee when creating objects. I did not need to fix imports



Prompt4: Write Python functions that:
- Add a new Employee to the list and save to CSV.
- Edit an existing Employee (but do not allow changing ID).
- Delete an Employee by index.
Include error handling.

AI Suggestion: 
from employee import Employee
from employee_csv import load_employees_from_csv, save_employees_to_csv


def create_employee(id, fname, lname, department, ph_number, filename="employee_data.csv"):
    """
    Create a new Employee and add to the CSV file.
    
    Args:
        id (int): Employee ID
        fname (str): First name
        lname (str): Last name
        department (str): Department code
        ph_number (str): Phone number
        filename (str): CSV file to save to
        
    Returns:
        Employee: The created Employee object
        
    Raises:
        ValueError: If employee data is invalid or ID already exists
        IOError: If unable to save to file
    """
    try:
        # Load existing employees to check for duplicate ID
        try:
            employees = load_employees_from_csv(filename)
        except FileNotFoundError:
            employees = []
        
        # Check if ID already exists
        for emp in employees:
            if emp.id == id:
                raise ValueError(f"Employee with ID {id} already exists")
        
        # Create new employee (this will validate all fields)
        new_employee = Employee(id, fname, lname, department, ph_number)
        
        # Add to list and save
        employees.append(new_employee)
        save_employees_to_csv(employees, filename)
        
        return new_employee
        
    except ValueError as e:
        raise ValueError(f"Cannot create employee: {e}")
    except IOError as e:
        raise IOError(f"Cannot save employee to file: {e}")


def edit_employee(index, fname=None, lname=None, department=None, ph_number=None, filename="employee_data.csv"):
    """
    Edit an existing Employee by index (ID cannot be changed).
    
    Args:
        index (int): Index of employee in the list (0-based)
        fname (str, optional): New first name
        lname (str, optional): New last name
        department (str, optional): New department code
        ph_number (str, optional): New phone number
        filename (str): CSV file to load from and save to
        
    Returns:
        Employee: The updated Employee object
        
    Raises:
        ValueError: If index is invalid or new data is invalid
        FileNotFoundError: If CSV file doesn't exist
        IOError: If unable to save to file
    """
    try:
        # Load existing employees
        employees = load_employees_from_csv(filename)
        
        # Check if index is valid
        if index < 0 or index >= len(employees):
            raise ValueError(f"Invalid employee index: {index}. Must be between 0 and {len(employees) - 1}")
        
        employee = employees[index]
        
        # Update fields if provided (validation happens in setters)
        if fname is not None:
            employee.fname = fname
        if lname is not None:
            employee.lname = lname
        if department is not None:
            employee.department = department
        if ph_number is not None:
            employee.ph_number = ph_number
        
        # Save updated list
        save_employees_to_csv(employees, filename)
        
        return employee
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Employee file '{filename}' not found")
    except ValueError as e:
        raise ValueError(f"Cannot edit employee: {e}")
    except IOError as e:
        raise IOError(f"Cannot save changes to file: {e}")


def delete_employee(index, filename="employee_data.csv"):
    """
    Delete an Employee by index.
    
    Args:
        index (int): Index of employee in the list (0-based)
        filename (str): CSV file to load from and save to
        
    Returns:
        Employee: The deleted Employee object
        
    Raises:
        ValueError: If index is invalid
        FileNotFoundError: If CSV file doesn't exist
        IOError: If unable to save to file
    """
    try:
        # Load existing employees
        employees = load_employees_from_csv(filename)
        
        # Check if index is valid
        if index < 0 or index >= len(employees):
            raise ValueError(f"Invalid employee index: {index}. Must be between 0 and {len(employees) - 1}")
        
        # Remove employee at index
        deleted_employee = employees.pop(index)
        
        # Save updated list
        save_employees_to_csv(employees, filename)
        
        return deleted_employee
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Employee file '{filename}' not found")
    except ValueError as e:
        raise ValueError(f"Cannot delete employee: {e}")
    except IOError as e:
        raise IOError(f"Cannot save changes to file: {e}")


def list_employees(filename="employee_data.csv"):
    """
    List all employees with their index numbers.
    
    Args:
        filename (str): CSV file to load from
        
    Returns:
        list: List of Employee objects
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
    """
    try:
        employees = load_employees_from_csv(filename)
        
        if not employees:
            print("No employees found.")
            return []
        
        print("Employee List:")
        print("-" * 80)
        for i, emp in enumerate(employees):
            print(f"Index {i}: {emp}")
        
        return employees
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Employee file '{filename}' not found")

Reflection: No human fixes needed


Prompt5: Write a Python function that prints a list of employees in the format:
1. ID - Last, First - Department - Phone

AI Suggestion: 
def display_employees(filename="employee_data.csv"):
    """
    Display employees in formatted list: ID - Last, First - Department - Phone
    
    Args:
        filename (str): CSV file to load from
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
    """
    try:
        employees = load_employees_from_csv(filename)
        
        if not employees:
            print("No employees found.")
            return
        
        for i, emp in enumerate(employees, 1):
            print(f"{i}. {emp.id} - {emp.lname}, {emp.fname} - {emp.department} - {emp.ph_number}")
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Employee file '{filename}' not found")

Reflection: Kept the validation rules inside employee class. Didn't have to change anything


Prompt6: Add test code to Employee class that tries valid and invalid data. Log errors to a file called employee_test.log.
Expected outcome: - Tests at the bottom of employee.py that create valid and invalid employees. - Errors logged to employee_test.log.

AI Suggestion: 
def display_employees(filename="employee_data.csv"):
    """
    Display employees in formatted list: ID - Last, First - Department - Phone
    
    Args:
        filename (str): CSV file to load from
        
    Raises:
        FileNotFoundError: If CSV file doesn't exist
    """
    try:
        employees = load_employees_from_csv(filename)
        
        if not employees:
            print("No employees found.")
            return
        
        for i, emp in enumerate(employees, 1):
            print(f"{i}. {emp.id} - {emp.lname}, {emp.fname} - {emp.department} - {emp.ph_number}")
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Employee file '{filename}' not found")

Prompt7: Create a subclass Manager(Employee) with an additional attribute (e.g., team_size or office_number). Override a method (such as __str__ or a display() method) to demonstrate polymorphism when listing employees.


AI Suggestion:
class Manager(Employee):
    """
    Manager class that inherits from Employee with additional attributes.

    Attributes:
        team_size (int): Number of team members managed
        office_number (str): Office number/location
    """

    def __init__(self, id, fname, lname, department, ph_number, team_size, office_number):
        """
        Initialize Manager object with validation.

        Args:
            id (str): Employee ID (read-only after creation)
            fname (str): First name
            lname (str): Last name
            department (str): Department code
            ph_number (str): Phone number
            team_size (int): Number of team members managed
            office_number (str): Office number/location

        Raises:
            ValueError: If any validation fails
        """
        super().__init__(id, fname, lname, department, ph_number)
        self.team_size = team_size
        self.office_number = office_number

    @property
    def team_size(self):
        """Get team size."""
        return self._team_size

    @team_size.setter
    def team_size(self, value):
        """
        Set team size with validation.

        Args:
            value (int): Team size

        Raises:
            ValueError: If team size is negative
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("Team size must be a non-negative integer")
        self._team_size = value

    @property
    def office_number(self):
        """Get office number."""
        return self._office_number

    @office_number.setter
    def office_number(self, value):
        """
        Set office number with validation.

        Args:
            value (str): Office number

        Raises:
            ValueError: If office number is empty
        """
        if not value or not value.strip():
            raise ValueError("Office number cannot be empty")
        self._office_number = value.strip()

    def __str__(self):
        """Return string representation of Manager (demonstrates polymorphism)."""
        return f"Manager(ID: {self._id}, Name: {self._fname} {self._lname}, Dept: {self._department}, Phone: {self.ph_number}, Team Size: {self._team_size}, Office: {self._office_number})"

    def __repr__(self):
        """Return detailed string representation of Manager."""
        return f"Manager({self._id}, '{self._fname}', '{self._lname}', '{self._department}', '{self._ph_number}', {self._team_size}, '{self._office_number}')"

Reflection : The AI correctly generated the code that I was looking for and no changes were made



Prompt8: Load the employees for manager subclass as well


AI Suggestion: 
def load_employees_from_csv(filename="employee_data.csv"):
    """
    Load Employee and Manager objects from a CSV file.

    Args:
        filename (str): Name of the CSV file to load from

    Returns:
        list: List of Employee and Manager objects

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If employee data is invalid
    """
    employees = []

    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Check if this is a Manager (has team_size and office_number)
                if 'team_size' in row and 'office_number' in row and row['team_size'] and row['office_number']:
                    employee = Manager(
                        id=row['id'],
                        fname=row['fname'],
                        lname=row['lname'],
                        department=row['department'],
                        ph_number=row['phNumber'],
                        team_size=int(row['team_size']),
                        office_number=row['office_number']
                    )
                else:
                    employee = Employee(
                        id=row['id'],
                        fname=row['fname'],
                        lname=row['lname'],
                        department=row['department'],
                        ph_number=row['phNumber']
                    )
                employees.append(employee)
                
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{filename}' not found")
    except KeyError as e:
        raise ValueError(f"Missing required column in CSV: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid employee data in CSV: {e}")
        
    return employees


def save_employees_to_csv(employees, filename="employee_data.csv"):
    """
    Save Employee and Manager objects to a CSV file.

    Args:
        employees (list): List of Employee and Manager objects to save
        filename (str): Name of the CSV file to save to

    Raises:
        IOError: If unable to write to the file
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'fname', 'lname', 'department', 'phNumber', 'team_size', 'office_number']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for employee in employees:
                row_data = {
                    'id': employee.id,
                    'fname': employee.fname,
                    'lname': employee.lname,
                    'department': employee.department,
                    'phNumber': employee._ph_number,  # Use raw digits for storage
                    'team_size': '',
                    'office_number': ''
                }

                # If this is a Manager, add the additional fields
                if isinstance(employee, Manager):
                    row_data['team_size'] = employee.team_size
                    row_data['office_number'] = employee.office_number

                writer.writerow(row_data)
                
    except IOError as e:
        raise IOError(f"Unable to write to CSV file '{filename}': {e}")

Reflection: Copilot added all the necessary function to include Manager(employee) to access the csv and to save the csv

Prompt: 
Implement functions for:
  o    Displaying the menu.
  o    Prompting for user input.
  o    Displaying employees in a clean 
  format.
  o    Showing messages to the user.
  •    The view should only handle 
  input/output — no business rules.

  AI Suggestion:
  """
Employee Management System - View Module

This module handles all user interface operations including:
- Menu display
- User input prompting
- Employee data display
- User message display

The view layer contains no business logic - only input/output operations.

Below is an example Menu output

Employee Management System
  1. Create New Employee
  2. Edit Existing Employee
  3. Delete Existing Employee
  4. Display Employees
  5. Quit
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
    print("\\")


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

AI Created the menu exactly as we wanted and everything works properly


Prompt9:
The whole project should be in MVC 
  (Model, View, Controller format). The 
  Model : Employee Class should be 
  employee.py and the Data layer should be 
  the csv stuff named EmployeeData.py and 
  the view layer should be named 
  EmployeeView.py

  AI Suggestion: It rearranged all the .py files to the right name and made only 3 files which were employee.py, EmployeeData.py and EmployeeView.py as per the requirements. It made different files names as the names weren't defined in the class exercise.

  Reflection: It rearranged all the .py files to the right name and made only 3 files which were employee.py, EmployeeData.py and EmployeeView.py as per the requirements. It made different files names as the names weren't defined in the class exercise.


Prompt10: 
Coordinate the Model, Data, and View.
  •	Implement menu options for:
  o	Create (validate input, save new employee).
  o	Edit (update employee attributes, but not ID).
  o	Delete (remove an employee).
  o	Display (list all employees).
  o	Quit.
  •	Handle errors gracefully and provide clear messages.
  •	Ensure the controller can handle both Employee and Manager objects (demonstrating polymorphism). which should be named EmployeeApp.py

  AI Suggestion: 
"""
Employee Management System - Controller Module

This module handles the business logic and coordinates between the Model and View layers.
It follows the MVC (Model-View-Controller) architecture pattern.

Controller responsibilities:
- Handle user interactions
- Coordinate between Model (employee.py) and Data (EmployeeData.py) layers
- Manage application flow and business logic
- Process user input and update views accordingly
"""

from employee import Employee, Manager
from EmployeeData import load_employees_from_csv, save_employees_to_csv
from EmployeeView import (
    display_menu, get_menu_choice, get_employee_data, display_employees,
    display_employee_details, show_message, confirm_action, get_employee_index,
    pause_for_user
)


class EmployeeController:
    """
    Main controller class that manages the Employee Management System.

    Attributes:
        employees (list): List of Employee and Manager objects
        filename (str): Current CSV filename being used
    """

    def __init__(self, filename="employee_data.csv"):
        """
        Initialize the controller with an empty employee list.

        Args:
            filename (str): Default CSV filename to use
        """
        self.employees = []
        self.filename = filename

    def run(self):
        """
        Main application loop - displays menu and handles user choices.
        """
        show_message("Welcome to the Employee Management System!", "info")

        # Try to load existing data
        self.load_employees()

        while True:
            display_menu()
            choice = get_menu_choice()

            if choice is None:
                continue

            if choice == 1:
                self.create_new_employee()
            elif choice == 2:
                self.edit_existing_employee()
            elif choice == 3:
                self.delete_existing_employee()
            elif choice == 4:
                self.display_employees()
            elif choice == 5:
                self.quit_application()
                break

    def create_new_employee(self):
        """
        Handle creating a new employee or manager.
        """
        try:
            # Ask if this is a manager or regular employee
            while True:
                emp_type = input("\nCreate (E)mployee or (M)anager? (E/M): ").strip().upper()
                if emp_type in ['E', 'M']:
                    break
                print("Please enter 'E' for Employee or 'M' for Manager.")

            is_manager = (emp_type == 'M')

            # Get employee data from view
            data = get_employee_data(is_manager)
            if data is None:
                show_message("Employee creation cancelled.", "info")
                return

            # Check for duplicate ID
            if self.find_employee_by_id(data['id']):
                show_message(f"Employee with ID '{data['id']}' already exists!", "error")
                return

            # Create the appropriate object
            if is_manager:
                new_employee = Manager(
                    data['id'], data['fname'], data['lname'],
                    data['department'], data['ph_number'],
                    data['team_size'], data['office_number']
                )
            else:
                new_employee = Employee(
                    data['id'], data['fname'], data['lname'],
                    data['department'], data['ph_number']
                )

            # Add to list
            self.employees.append(new_employee)

            # Auto-save
            self.save_employees()

            show_message(f"{'Manager' if is_manager else 'Employee'} '{data['fname']} {data['lname']}' created successfully!", "success")
            display_employee_details(new_employee)

        except ValueError as e:
            show_message(f"Error creating employee: {e}", "error")
        except Exception as e:
            show_message(f"Unexpected error: {e}", "error")

        pause_for_user()

    def edit_existing_employee(self):
        """
        Handle editing an existing employee.
        """
        if not self.employees:
            show_message("No employees found. Please create an employee first.", "info")
            pause_for_user()
            return

        try:
            # Display current employees
            display_employees(self.employees, "Select Employee to Edit")

            # Get employee selection
            index = get_employee_index(len(self.employees))
            if index is None:
                show_message("Edit cancelled.", "info")
                pause_for_user()
                return

            employee = self.employees[index]
            is_manager = isinstance(employee, Manager)

            show_message(f"Editing {'Manager' if is_manager else 'Employee'}: {employee.fname} {employee.lname}", "info")
            display_employee_details(employee, index)

            # Get new data (allow empty values to keep current)
            print("\nEnter new values (press Enter to keep current value):")

            # Get new first name
            new_fname = input(f"First Name ({employee.fname}): ").strip()
            if new_fname:
                employee.fname = new_fname

            # Get new last name
            new_lname = input(f"Last Name ({employee.lname}): ").strip()
            if new_lname:
                employee.lname = new_lname

            # Get new department
            new_dept = input(f"Department ({employee.department}): ").strip()
            if new_dept:
                employee.department = new_dept

            # Get new phone number
            new_phone = input(f"Phone Number ({employee.ph_number}): ").strip()
            if new_phone:
                employee.ph_number = new_phone

            # Manager-specific fields
            if is_manager:
                new_team_size = input(f"Team Size ({employee.team_size}): ").strip()
                if new_team_size:
                    employee.team_size = int(new_team_size)

                new_office = input(f"Office Number ({employee.office_number}): ").strip()
                if new_office:
                    employee.office_number = new_office

            # Auto-save
            self.save_employees()

            show_message("Employee updated successfully!", "success")
            display_employee_details(employee)

        except ValueError as e:
            show_message(f"Error updating employee: {e}", "error")
        except Exception as e:
            show_message(f"Unexpected error: {e}", "error")

        pause_for_user()

    def delete_existing_employee(self):
        """
        Handle deleting an existing employee.
        """
        if not self.employees:
            show_message("No employees found.", "info")
            pause_for_user()
            return

        try:
            # Display current employees
            display_employees(self.employees, "Select Employee to Delete")

            # Get employee selection
            index = get_employee_index(len(self.employees))
            if index is None:
                show_message("Delete cancelled.", "info")
                pause_for_user()
                return

            employee = self.employees[index]

            # Confirm deletion
            if confirm_action(f"delete {employee.fname} {employee.lname} (ID: {employee.id})"):
                deleted_employee = self.employees.pop(index)

                # Auto-save
                self.save_employees()

                show_message(f"Employee '{deleted_employee.fname} {deleted_employee.lname}' deleted successfully!", "success")
            else:
                show_message("Delete cancelled.", "info")

        except Exception as e:
            show_message(f"Error deleting employee: {e}", "error")

        pause_for_user()

    def display_employees(self):
        """
        Handle displaying all employees.
        """
        if not self.employees:
            show_message("No employees found.", "info")
        else:
            display_employees(self.employees, f"All Employees ({len(self.employees)} total)")

            # Offer to show details for specific employee
            if len(self.employees) > 0:
                show_details = input("\nShow details for specific employee? (y/n): ").strip().lower()
                if show_details in ['y', 'yes']:
                    index = get_employee_index(len(self.employees))
                    if index is not None:
                        display_employee_details(self.employees[index], index)

        pause_for_user()

    def load_employees(self):
        """
        Load employees from CSV file.
        """
        try:
            self.employees = load_employees_from_csv(self.filename)
            if self.employees:
                show_message(f"Loaded {len(self.employees)} employees from '{self.filename}'", "success")
            else:
                show_message(f"No existing data found in '{self.filename}'. Starting fresh.", "info")
        except FileNotFoundError:
            show_message(f"No existing file '{self.filename}' found. Starting with empty database.", "info")
        except Exception as e:
            show_message(f"Error loading employees: {e}", "error")

    def save_employees(self):
        """
        Save employees to CSV file.
        """
        try:
            save_employees_to_csv(self.employees, self.filename)
        except Exception as e:
            show_message(f"Error saving employees: {e}", "error")

    def find_employee_by_id(self, emp_id):
        """
        Find an employee by ID.

        Args:
            emp_id (str): Employee ID to search for

        Returns:
            Employee/Manager object if found, None otherwise
        """
        for employee in self.employees:
            if employee.id == emp_id:
                return employee
        return None

    def quit_application(self):
        """
        Handle application shutdown.
        """
        if confirm_action("quit the application"):
            # Final save
            self.save_employees()
            show_message("Thank you for using the Employee Management System!", "info")
        else:
            show_message("Returning to main menu.", "info")


def main():
    """
    Entry point for the Employee Management System.
    """
    controller = EmployeeController()
    controller.run()


Reflection: Copilot suggested a great set of code which is already working and I did not have to do extra work except for reading through it to see if its right.

Prompt11:
Add a simple pytest test file with 1–2 unit tests for your Employee/Manager classes.

AI Suggestion: 
"""
Pytest unit tests for Employee and Manager classes.

This module demonstrates modern automated testing practices using pytest.
Run with: pytest test_employee.py -v

Requirements:
- pytest (install with: pip install pytest)
"""

import pytest
from employee import Employee, Manager


class TestEmployee:
    """Test cases for the Employee class."""

    def test_valid_employee_creation(self):
        """Test that a valid employee can be created successfully."""
        emp = Employee("E001", "John", "Doe", "ENG", "5551234567")

        assert emp.id == "E001"
        assert emp.fname == "John"
        assert emp.lname == "Doe"
        assert emp.department == "ENG"
        assert emp.getphNumber() == "5551234567"
        assert emp.ph_number == "(555)123-4567"

    def test_phone_number_sanitization(self):
        """Test that phone numbers are properly sanitized from various formats."""
        test_cases = [
            ("(555) 123-4567", "5551234567"),
            ("555.123.4567", "5551234567"),
            ("555-123-4567", "5551234567"),
            ("5551234567", "5551234567"),
            ("(555)123-4567", "5551234567"),
        ]

        for formatted_phone, expected_digits in test_cases:
            emp = Employee("TEST", "Test", "User", "TST", formatted_phone)
            assert emp.getphNumber() == expected_digits
            assert emp.ph_number == "(555)123-4567"

    def test_invalid_first_name(self):
        """Test that invalid first names raise ValueError."""
        # Empty first name
        with pytest.raises(ValueError, match="First name cannot be empty"):
            Employee("E001", "", "Doe", "ENG", "5551234567")

        # First name with digits
        with pytest.raises(ValueError, match="First name cannot contain digits"):
            Employee("E001", "John123", "Doe", "ENG", "5551234567")

    def test_invalid_last_name(self):
        """Test that invalid last names raise ValueError."""
        # Empty last name
        with pytest.raises(ValueError, match="Last name cannot be empty"):
            Employee("E001", "John", "", "ENG", "5551234567")

        # Last name with digits
        with pytest.raises(ValueError, match="Last name cannot contain digits"):
            Employee("E001", "John", "Doe123", "ENG", "5551234567")

    def test_invalid_department(self):
        """Test that invalid departments raise ValueError."""
        # Too short (2 characters)
        with pytest.raises(ValueError, match="Department must be exactly 3 characters"):
            Employee("E001", "John", "Doe", "EN", "5551234567")

        # Too long (4 characters)
        with pytest.raises(ValueError, match="Department must be exactly 3 characters"):
            Employee("E001", "John", "Doe", "ENGR", "5551234567")

        # Lowercase
        with pytest.raises(ValueError, match="Department must be uppercase letters"):
            Employee("E001", "John", "Doe", "eng", "5551234567")

        # Contains digits
        with pytest.raises(ValueError, match="Department must contain only letters"):
            Employee("E001", "John", "Doe", "E1G", "5551234567")

    def test_invalid_phone_number(self):
        """Test that invalid phone numbers raise ValueError."""
        # Too short
        with pytest.raises(ValueError, match="Phone number must contain exactly 10 digits"):
            Employee("E001", "John", "Doe", "ENG", "12345")

        # Too long
        with pytest.raises(ValueError, match="Phone number must contain exactly 10 digits"):
            Employee("E001", "John", "Doe", "ENG", "12345678901")

        # Contains letters
        with pytest.raises(ValueError, match="Phone number must contain exactly 10 digits"):
            Employee("E001", "John", "Doe", "ENG", "555-abc-1234")

        # Empty
        with pytest.raises(ValueError, match="Phone number cannot be empty"):
            Employee("E001", "John", "Doe", "ENG", "")

    def test_id_is_read_only(self):
        """Test that employee ID cannot be modified after creation."""
        emp = Employee("E001", "John", "Doe", "ENG", "5551234567")

        # Attempting to modify ID should raise AttributeError
        with pytest.raises(AttributeError, match="Employee ID is read-only"):
            emp._id = "MODIFIED"

    def test_employee_string_representation(self):
        """Test the string representation of Employee objects."""
        emp = Employee("E001", "John", "Doe", "ENG", "5551234567")
        expected = "Employee(ID: E001, Name: John Doe, Dept: ENG, Phone: (555)123-4567)"
        assert str(emp) == expected


class TestManager:
    """Test cases for the Manager class."""

    def test_valid_manager_creation(self):
        """Test that a valid manager can be created successfully."""
        mgr = Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "A-201")

        assert mgr.id == "M001"
        assert mgr.fname == "Jane"
        assert mgr.lname == "Smith"
        assert mgr.department == "ITM"
        assert mgr.getphNumber() == "5559876543"
        assert mgr.team_size == 5
        assert mgr.office_number == "A-201"

    def test_manager_inherits_from_employee(self):
        """Test that Manager properly inherits from Employee."""
        mgr = Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "A-201")

        # Should have all Employee functionality
        assert isinstance(mgr, Employee)
        assert mgr.getphNumber() == "5559876543"
        assert mgr.ph_number == "(555)987-6543"

    def test_invalid_team_size(self):
        """Test that invalid team sizes raise ValueError."""
        # Negative team size
        with pytest.raises(ValueError, match="Team size must be a non-negative integer"):
            Manager("M001", "Jane", "Smith", "ITM", "5559876543", -1, "A-201")

        # Non-integer team size
        with pytest.raises(ValueError, match="Team size must be a non-negative integer"):
            Manager("M001", "Jane", "Smith", "ITM", "5559876543", "five", "A-201")

    def test_invalid_office_number(self):
        """Test that invalid office numbers raise ValueError."""
        # Empty office number
        with pytest.raises(ValueError, match="Office number cannot be empty"):
            Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "")

        # None office number
        with pytest.raises(ValueError, match="Office number cannot be empty"):
            Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, None)

    def test_manager_string_representation_polymorphism(self):
        """Test that Manager has different string representation (polymorphism)."""
        emp = Employee("E001", "John", "Doe", "ENG", "5551234567")
        mgr = Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "A-201")

        # Different string representations demonstrate polymorphism
        emp_str = str(emp)
        mgr_str = str(mgr)

        assert "Employee(ID: E001" in emp_str
        assert "Manager(ID: M001" in mgr_str
        assert "Team Size: 5" in mgr_str
        assert "Office: A-201" in mgr_str
        assert "Team Size" not in emp_str
        assert "Office" not in emp_str

    def test_manager_property_setters(self):
        """Test that Manager property setters work correctly."""
        mgr = Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "A-201")

        # Test valid updates
        mgr.team_size = 10
        assert mgr.team_size == 10

        mgr.office_number = "B-305"
        assert mgr.office_number == "B-305"

        # Test office number trimming
        mgr.office_number = "  C-101  "
        assert mgr.office_number == "C-101"


class TestPolymorphism:
    """Test cases demonstrating polymorphism between Employee and Manager."""

    def test_polymorphic_behavior(self):
        """Test that Employee and Manager objects behave differently via polymorphism."""
        employees = [
            Employee("E001", "John", "Doe", "ENG", "5551111111"),
            Manager("M001", "Jane", "Smith", "ITM", "5552222222", 3, "A-301")
        ]

        # Same method call, different behavior based on object type
        string_representations = [str(emp) for emp in employees]

        # Employee string should not have manager-specific info
        assert "Team Size" not in string_representations[0]
        assert "Office" not in string_representations[0]

        # Manager string should have manager-specific info
        assert "Team Size: 3" in string_representations[1]
        assert "Office: A-301" in string_representations[1]

    def test_isinstance_inheritance(self):
        """Test that Manager is an instance of Employee (inheritance)."""
        emp = Employee("E001", "John", "Doe", "ENG", "5551234567")
        mgr = Manager("M001", "Jane", "Smith", "ITM", "5559876543", 5, "A-201")

        assert isinstance(emp, Employee)
        assert not isinstance(emp, Manager)
        assert isinstance(mgr, Employee)  # Manager IS-A Employee
        assert isinstance(mgr, Manager)


if __name__ == "__main__":
    # Allow running tests directly with python
    pytest.main([__file__, "-v"])

Reflection: Copilot made what I asked for no changes