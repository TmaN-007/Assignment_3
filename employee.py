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