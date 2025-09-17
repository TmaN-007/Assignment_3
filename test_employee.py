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