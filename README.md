# Employee Management System

A comprehensive Employee Management System built with Python following the MVC (Model-View-Controller) architecture pattern. The system supports both Employee and Manager objects with inheritance, polymorphism, and automated testing.

## Project Structure

```
Employee-Management-System/
├── employee.py          # Model - Employee and Manager classes
├── EmployeeData.py      # Data layer - CSV persistence
├── EmployeeView.py      # View layer - User interface functions
├── EmployeeApp.py       # Controller - Business logic and coordination
├── test_employee.py     # Pytest unit tests
├── employee_test.log    # Test execution log
└── README.md           # This file
```

## Getting Started

### Prerequisites

- Python 3.x
- pytest (for running unit tests)

```bash
# Install pytest (optional, for running tests)
pip install pytest
```

### Running the Application

#### Option 1: Interactive Employee Management System
```bash
python3 EmployeeApp.py
```

#### Option 2: Run Employee/Manager Class Tests
```bash
python3 employee.py
```

#### Option 3: Run Automated Unit Tests
```bash
# With pytest (recommended)
pytest test_employee.py -v

# Or run directly
python3 test_employee.py
```

## Step-by-Step Instructions

### 1. Starting the Application

```bash
$ python3 EmployeeApp.py
```

**Expected Output:**
```
Welcome to the Employee Management System!
No existing file 'employee_data.csv' found. Starting with empty database.

Employee Management System
1. Create New Employee
2. Edit Existing Employee
3. Delete Existing Employee
4. Display Employees
5. Quit
\

Select an option (1-5):
```

### 2. Creating a New Employee

**Input:** Select option `1`
```
Select an option (1-5): 1

Create (E)mployee or (M)anager? (E/M): E

Enter Employee Information:
----------------------------------------
Employee ID: E001
First Name: John
Last Name: Doe
Department (3 uppercase letters): ENG
Phone Number (any format): (555) 123-4567
```

**Expected Output:**
```
Employee 'John Doe' created successfully!

Employee Details
----------------------------------------
ID: E001
Name: John Doe
Department: ENG
Phone (Formatted): (555)123-4567
Phone (Unformatted): 5551234567

Press Enter to continue...
```

### 3. Creating a Manager

**Input:** Select option `1`, then `M`
```
Select an option (1-5): 1

Create (E)mployee or (M)anager? (E/M): M

Enter Manager Information:
----------------------------------------
Employee ID: M001
First Name: Jane
Last Name: Smith
Department (3 uppercase letters): ITM
Phone Number (any format): 555.987.6543
Team Size: 5
Office Number: A-201
```

**Expected Output:**
```
Manager 'Jane Smith' created successfully!

Manager Details
----------------------------------------
ID: M001
Name: Jane Smith
Department: ITM
Phone (Formatted): (555)987-6643
Phone (Unformatted): 5559876543
Team Size: 5
Office: A-201

Press Enter to continue...
```

### 4. Displaying All Employees

**Input:** Select option `4`

**Expected Output:**
```
All Employees (2 total)
====================================================================================================
#   ID       Name                      Dept   Phone           Type       Details
----------------------------------------------------------------------------------------------------
1   E001     John Doe                  ENG    (555)123-4567   Employee
2   M001     Jane Smith                ITM    (555)987-6643   Manager    Team:5, Office:A-201
----------------------------------------------------------------------------------------------------
Total: 2 employees

Show details for specific employee? (y/n): n

Press Enter to continue...
```

### 5. Editing an Employee

**Input:** Select option `2`
```
Select an option (1-5): 2

Select Employee to Edit
====================================================================================================
#   ID       Name                      Dept   Phone           Type       Details
----------------------------------------------------------------------------------------------------
1   E001     John Doe                  ENG    (555)123-4567   Employee
2   M001     Jane Smith                ITM    (555)987-6643   Manager    Team:5, Office:A-201
----------------------------------------------------------------------------------------------------
Total: 2 employees

Enter employee number (1-2): 1

Editing Employee: John Doe

Employee Details (Index: 0)
----------------------------------------
ID: E001
Name: John Doe
Department: ENG
Phone (Formatted): (555)123-4567
Phone (Unformatted): 5551234567

Enter new values (press Enter to keep current value):
First Name (John): Johnny
Last Name (Doe):
Department (ENG):
Phone Number ((555)123-4567):

Employee updated successfully!
```

### 6. Viewing CSV Data

The system automatically saves data to `employee_data.csv`:

```csv
id,fname,lname,department,phNumber,employee_type,team_size,office_number
E001,Johnny,Doe,ENG,5551234567,E,,
M001,Jane,Smith,ITM,5559876543,M,5,A-201
```

### 7. Running Class Tests

**Input:**
```bash
python3 employee.py
```

**Sample Output:**
```
============================================================
EMPLOYEE AND MANAGER CLASS TESTING
============================================================

1. Testing Valid Employee Creation:
Created: Employee(ID: E001, Name: John Doe, Dept: ENG, Phone: (555)123-4567)
  Formatted phone: (555)123-4567
  Unformatted phone: 5551234567

2. Testing Valid Manager Creation:
Created: Manager(ID: M001, Name: Jane Smith, Dept: ITM, Phone: (555)987-6643, Team Size: 8, Office: A-205)
  Team size: 8
  Office: A-205

3. Testing Invalid Employee Creation:
Expected error - Empty first name: First name cannot be empty
Expected error - Digits in first name: First name cannot contain digits
[... more validation tests ...]

============================================================
TESTING COMPLETED
============================================================
Check 'employee_test.log' for detailed logs with timestamps.
```

## System Architecture

### MVC Pattern Implementation

- **Model (`employee.py`)**: Employee and Manager classes with business rules
- **View (`EmployeeView.py`)**: User interface functions (input/output only)
- **Controller (`EmployeeApp.py`)**: Business logic and coordination
- **Data (`EmployeeData.py`)**: CSV persistence layer

### Key Features

#### Employee Class
- String ID (read-only after creation)
- Name validation (no digits, not empty)
- Department validation (exactly 3 uppercase letters)
- Phone number sanitization (accepts multiple formats)
- @property decorators for all attributes

#### Manager Class (Inheritance & Polymorphism)
- Inherits from Employee
- Additional attributes: team_size, office_number
- Polymorphic string representation
- Full validation for manager-specific attributes

#### Data Persistence
- CSV format with employee type indicator ('E' or 'M')
- Automatic object type detection and restoration
- Phone number stored as unformatted digits

## Testing

### Automated Unit Tests

Run comprehensive pytest tests:
```bash
pytest test_employee.py -v
```

**Sample Test Output:**
```
test_employee.py::TestEmployee::test_valid_employee_creation PASSED
test_employee.py::TestEmployee::test_phone_number_sanitization PASSED
test_employee.py::TestEmployee::test_invalid_first_name PASSED
test_employee.py::TestManager::test_valid_manager_creation PASSED
test_employee.py::TestPolymorphism::test_polymorphic_behavior PASSED
========================== 16 passed in 0.05s ==========================
```

### Manual Testing

Run built-in class tests with logging:
```bash
python3 employee.py
```

Tests are logged to `employee_test.log` with timestamps.

## Validation Rules

### Employee Validation
- **ID**: Any string (read-only after creation)
- **First/Last Name**: Cannot be empty, no digits allowed
- **Department**: Exactly 3 uppercase letters
- **Phone**: Must contain exactly 10 digits (auto-sanitized from various formats)

### Manager Additional Validation
- **Team Size**: Non-negative integer
- **Office Number**: Cannot be empty

### Phone Number Formats Accepted
- `(555) 123-4567`
- `555.123.4567`
- `555-123-4567`
- `5551234567`
- `555 123 4567`

All formats are sanitized to 10-digit storage and formatted as `(555)123-4567` for display.

## Sample Error Handling

### Invalid Input Examples

```bash
# Invalid department
Department (3 uppercase letters): engineering
Department must be exactly 3 characters

# Invalid phone number
Phone Number (any format): 555-abc-1234
Phone number must contain exactly 10 digits

# Invalid name
First Name: John123
First name cannot contain digits
```

## Key Benefits

- **Clean Architecture**: Proper MVC separation of concerns
- **Type Safety**: Strong validation with clear error messages
- **User Friendly**: Accepts multiple phone number formats
- **Polymorphism**: Different behavior for Employee vs Manager
- **Automated Testing**: Comprehensive test coverage
- **Data Integrity**: CSV format preserves object types
- **Logging**: Detailed test execution logs with timestamps

## Notes

- CSV files are automatically created in the same directory as the Python files
- The system starts fresh if no CSV file exists
- All changes are automatically saved to CSV
- Test logs are written to `employee_test.log`
- Phone numbers are stored as 10 digits but displayed formatted