import csv
from employee import Employee, Manager


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