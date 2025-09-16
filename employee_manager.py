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