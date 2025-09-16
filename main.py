#!/usr/bin/env python3
"""
Main script to demonstrate Employee management system functionality.
This file can be used for debugging the Employee class and related functions.
"""

from employee import Employee
from employee_csv import load_employees_from_csv, save_employees_to_csv
from employee_manager import create_employee, edit_employee, delete_employee, list_employees, display_employees
import logging

# Configure logging for debugging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

def test_employee_creation():
    """Test creating valid and invalid employees."""
    logging.info("Testing employee creation...")
    
    # Test valid employee
    try:
        emp1 = Employee(1, "John", "Doe", "ENG", "1234567890")
        logging.info(f"Valid employee created: {emp1}")
        print(f"✓ Valid employee: {emp1}")
    except Exception as e:
        logging.error(f"Failed to create valid employee: {e}")
        print(f"✗ Failed to create valid employee: {e}")
    
    # Test invalid employees
    invalid_tests = [
        (2, "", "Smith", "ENG", "1234567890"),  # Empty first name
        (3, "Jane123", "Doe", "ENG", "1234567890"),  # Digits in name
        (4, "Bob", "Johnson", "ENGR", "1234567890"),  # Invalid department
        (5, "Alice", "Brown", "ENG", "12345"),  # Invalid phone
    ]
    
    for test_data in invalid_tests:
        try:
            emp = Employee(*test_data)
            logging.warning(f"Should have failed but created: {emp}")
            print(f"⚠ Should have failed: {emp}")
        except Exception as e:
            logging.info(f"Expected validation error: {e}")
            print(f"✓ Expected validation error: {e}")

def test_csv_operations():
    """Test CSV loading and saving operations."""
    logging.info("Testing CSV operations...")
    
    try:
        # Create some test employees
        employees = [
            Employee(1, "John", "Doe", "ENG", "1234567890"),
            Employee(2, "Jane", "Smith", "HR", "0987654321"),
            Employee(3, "Bob", "Johnson", "IT", "5555555555")
        ]
        
        # Save to CSV
        save_employees_to_csv(employees, "test_employees.csv")
        logging.info("Employees saved to CSV")
        print("✓ Employees saved to CSV")
        
        # Load from CSV
        loaded_employees = load_employees_from_csv("test_employees.csv")
        logging.info(f"Loaded {len(loaded_employees)} employees from CSV")
        print(f"✓ Loaded {len(loaded_employees)} employees from CSV")
        
        # Display employees
        print("\nEmployee List:")
        display_employees("test_employees.csv")
        
    except Exception as e:
        logging.error(f"CSV operations failed: {e}")
        print(f"✗ CSV operations failed: {e}")

def test_employee_management():
    """Test employee management functions."""
    logging.info("Testing employee management...")
    
    try:
        # Create a new employee
        new_emp = create_employee(100, "Alice", "Wilson", "FIN", "1111111111", "test_employees.csv")
        logging.info(f"Created new employee: {new_emp}")
        print(f"✓ Created new employee: {new_emp}")
        
        # List all employees
        print("\nAll employees:")
        list_employees("test_employees.csv")
        
        # Edit an employee
        edited_emp = edit_employee(0, fname="Johnny", filename="test_employees.csv")
        logging.info(f"Edited employee: {edited_emp}")
        print(f"✓ Edited employee: {edited_emp}")
        
        # Delete an employee
        deleted_emp = delete_employee(3, "test_employees.csv")
        logging.info(f"Deleted employee: {deleted_emp}")
        print(f"✓ Deleted employee: {deleted_emp}")
        
    except Exception as e:
        logging.error(f"Employee management failed: {e}")
        print(f"✗ Employee management failed: {e}")

def main():
    """Main function to run all tests."""
    print("=== Employee Management System Debug Tests ===\n")
    
    # Set breakpoints on these lines for debugging
    test_employee_creation()
    print("\n" + "="*50 + "\n")
    
    test_csv_operations()
    print("\n" + "="*50 + "\n")
    
    test_employee_management()
    print("\n" + "="*50 + "\n")
    
    print("Debug tests completed. Check debug.log for detailed logs.")

if __name__ == "__main__":
    main()
