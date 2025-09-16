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

