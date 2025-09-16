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