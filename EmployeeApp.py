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


if __name__ == "__main__":
    controller = EmployeeController()
    controller.run()