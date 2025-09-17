class Employee:
    """
    Employee class to manage employee information with validation.

    Attributes:
        _id (str): Employee ID
        _fname (str): First name (cannot be empty or contain digits)
        _lname (str): Last name (cannot be empty or contain digits)
        _department (str): Department code (exactly 3 uppercase letters)
        _ph_number (str): Phone number (exactly 10 digits)
    """
    
    def __init__(self, id, fname, lname, department, ph_number):
        """
        Initialize Employee object with validation.

        Args:
            id (str): Employee ID (read-only after creation)
            fname (str): First name
            lname (str): Last name
            department (str): Department code
            ph_number (str): Phone number

        Raises:
            ValueError: If any validation fails
        """
        object.__setattr__(self, '_id', str(id))
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
        Set phone number with validation and sanitization.
        Accepts formatted phone numbers and sanitizes them to 10 digits.

        Args:
            value (str): Phone number (can be formatted)

        Raises:
            ValueError: If phone number doesn't contain exactly 10 digits
        """
        import re

        if not value:
            raise ValueError("Phone number cannot be empty")

        # Remove all non-digit characters
        digits_only = re.sub(r'\D', '', value)

        if len(digits_only) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")

        self._ph_number = digits_only

    def getphNumber(self):
        """
        Return the unformatted 10-digit phone number.

        Returns:
            str: Phone number as 10 digits
        """
        return self._ph_number

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


if __name__ == "__main__":
    import logging

    # Configure logging to file with timestamp
    logging.basicConfig(
        filename='employee_test.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'  # Overwrite log file each time
    )

    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

    logger = logging.getLogger(__name__)

    print("="*60)
    print("EMPLOYEE AND MANAGER CLASS TESTING")
    print("="*60)

    # Test 1: Valid Employee Creation
    print("\n1. Testing Valid Employee Creation:")
    try:
        emp1 = Employee("E001", "John", "Doe", "ENG", "(555) 123-4567")
        logger.info(f"✓ Valid Employee created: {emp1}")
        print(f"✓ Created: {emp1}")
        print(f"  Formatted phone: {emp1.ph_number}")
        print(f"  Unformatted phone: {emp1.getphNumber()}")
    except ValueError as e:
        logger.error(f"✗ Unexpected error creating valid employee: {e}")
        print(f"✗ Error: {e}")

    # Test 2: Valid Manager Creation
    print("\n2. Testing Valid Manager Creation:")
    try:
        mgr1 = Manager("M001", "Jane", "Smith", "ITM", "555.987.6543", 8, "A-205")
        logger.info(f"✓ Valid Manager created: {mgr1}")
        print(f"✓ Created: {mgr1}")
        print(f"  Team size: {mgr1.team_size}")
        print(f"  Office: {mgr1.office_number}")
    except ValueError as e:
        logger.error(f"✗ Unexpected error creating valid manager: {e}")
        print(f"✗ Error: {e}")

    # Test 3: Invalid Employee Tests
    print("\n3. Testing Invalid Employee Creation:")

    invalid_employee_tests = [
        # (id, fname, lname, dept, phone, description)
        ("E002", "", "Smith", "ENG", "1234567890", "Empty first name"),
        ("E003", "Bob123", "Johnson", "ENG", "1234567890", "Digits in first name"),
        ("E004", "Alice", "Brown456", "ENG", "1234567890", "Digits in last name"),
        ("E005", "Charlie", "Wilson", "ENGR", "1234567890", "Invalid department (4 chars)"),
        ("E006", "David", "Garcia", "eng", "1234567890", "Lowercase department"),
        ("E007", "Eva", "Martinez", "E1G", "1234567890", "Department with digit"),
        ("E008", "Frank", "Lopez", "ENG", "12345", "Phone too short"),
        ("E009", "Grace", "Anderson", "ENG", "12345678901", "Phone too long"),
        ("E010", "Henry", "Taylor", "ENG", "555-abc-1234", "Phone with letters"),
        ("E011", "Iris", "Moore", "ENG", "", "Empty phone number"),
    ]

    for test_data in invalid_employee_tests:
        emp_id, fname, lname, dept, phone, description = test_data
        try:
            emp = Employee(emp_id, fname, lname, dept, phone)
            logger.warning(f"⚠ Should have failed but created employee for test: {description}")
            print(f"⚠ UNEXPECTED SUCCESS: {description} - {emp}")
        except ValueError as e:
            logger.error(f"✓ Expected validation error for {description}: {e}")
            print(f"✓ Expected error - {description}: {e}")

    # Test 4: Invalid Manager Tests
    print("\n4. Testing Invalid Manager Creation:")

    invalid_manager_tests = [
        # (id, fname, lname, dept, phone, team_size, office, description)
        ("M002", "John", "Manager", "ITM", "5551234567", -1, "B-101", "Negative team size"),
        ("M003", "Jane", "Boss", "ITM", "5551234567", "five", "B-102", "Non-integer team size"),
        ("M004", "Mike", "Lead", "ITM", "5551234567", 5, "", "Empty office number"),
        ("M005", "Sarah", "Director", "ITM", "5551234567", 10, None, "None office number"),
    ]

    for test_data in invalid_manager_tests:
        mgr_id, fname, lname, dept, phone, team_size, office, description = test_data
        try:
            mgr = Manager(mgr_id, fname, lname, dept, phone, team_size, office)
            logger.warning(f"⚠ Should have failed but created manager for test: {description}")
            print(f"⚠ UNEXPECTED SUCCESS: {description} - {mgr}")
        except (ValueError, TypeError) as e:
            logger.error(f"✓ Expected validation error for {description}: {e}")
            print(f"✓ Expected error - {description}: {e}")

    # Test 5: Phone Number Sanitization
    print("\n5. Testing Phone Number Sanitization:")
    phone_formats = [
        "(555) 123-4567",
        "555.123.4567",
        "555-123-4567",
        "5551234567",
        "(555)123-4567",
        "555 123 4567"
    ]

    for i, phone_format in enumerate(phone_formats, 1):
        try:
            emp = Employee(f"P{i:03d}", "Test", "User", "TST", phone_format)
            logger.info(f"✓ Phone sanitization: '{phone_format}' → stored as '{emp.getphNumber()}' → formatted as '{emp.ph_number}'")
            print(f"✓ '{phone_format}' → '{emp.getphNumber()}' → '{emp.ph_number}'")
        except ValueError as e:
            logger.error(f"✗ Phone sanitization failed for '{phone_format}': {e}")
            print(f"✗ Failed: '{phone_format}' - {e}")

    # Test 6: ID Read-Only Test
    print("\n6. Testing ID Read-Only Property:")
    try:
        emp = Employee("R001", "Read", "Only", "TST", "5551234567")
        original_id = emp.id
        logger.info(f"✓ Employee created with ID: {original_id}")

        # Try to modify ID (should fail)
        try:
            emp._id = "MODIFIED"
            logger.error(f"✗ ID modification should have failed but succeeded")
            print("✗ ID modification unexpectedly succeeded")
        except AttributeError as e:
            logger.info(f"✓ ID modification correctly prevented: {e}")
            print(f"✓ ID is read-only: {e}")

    except Exception as e:
        logger.error(f"✗ Error in read-only test: {e}")

    # Test 7: Polymorphism Demonstration
    print("\n7. Testing Polymorphism:")
    try:
        employees = [
            Employee("P001", "Poly", "Employee", "ENG", "5551111111"),
            Manager("P002", "Poly", "Manager", "ITM", "5552222222", 3, "C-301")
        ]

        logger.info("✓ Polymorphism demonstration:")
        print("✓ Polymorphism demonstration:")
        for emp in employees:
            # Same method call, different behavior based on object type
            logger.info(f"  {type(emp).__name__}: {emp}")
            print(f"  {type(emp).__name__}: {emp}")

    except Exception as e:
        logger.error(f"✗ Polymorphism test failed: {e}")

    print("\n" + "="*60)
    print("TESTING COMPLETED")
    print("="*60)
    print("Check 'employee_test.log' for detailed logs with timestamps.")
    logger.info("All tests completed successfully!")