# Assignment-
Tutedude assignment 
# Step 1: Plan the Data Storage and Initialize
employees = {
    101: {
        'name': 'Satya',
        'age': 27,
        'department': 'HR',
        'salary': 50000
    },
    102: {
        'name': 'Priya',
        'age': 32,
        'department': 'Engineering',
        'salary': 75000
    },
    103: {
        'name': 'Rahul',
        'age': 45,
        'department': 'Sales',
        'salary': 90000
    }
}

# ---
# Step 3: Add Employee Functionality
def add_employee():
    """
    Prompts the user for a new employee's details and adds them to the dictionary.
    Ensures the employee ID is unique.
    """
    print("\n--- Add New Employee ---")
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Error: Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical ID.")

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Monthly Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"\nEmployee {name} with ID {emp_id} successfully added.")

# ---
# Step 4: View All Employees
def view_employees():
    """
    Displays all employees in a formatted, table-like structure.
    """
    print("\n--- All Employees ---")
    if not employees:
        print("No employees available.")
        return

    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Department':<15} | {'Salary':<10}")
    print("-" * 65)
    for emp_id, data in employees.items():
        print(f"{emp_id:<5} | {data['name']:<20} | {data['age']:<5} | {data['department']:<15} | ${data['salary']:<9,}")

# ---
# Step 5: Search for an Employee by ID
def search_employee():
    """
    Prompts for an employee ID and displays their details if found.
    """
    print("\n--- Search for Employee ---")
    try:
        emp_id = int(input("Enter the Employee ID to search for: "))
    except ValueError:
        print("Invalid input. Please enter a numerical ID.")
        return

    if emp_id in employees:
        data = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"ID: {emp_id}")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Department: {data['department']}")
        print(f"Salary: ${data['salary']}")
    else:
        print(f"Error: Employee with ID {emp_id} not found.")

# ---
# Step 2 & 6: Define the Menu System & Exit the Program
def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    while True:
        print("\n===============================")
        print("  Employee Management System")
        print("===============================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        print("-------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main program
if __name__ == "__main__":
    main_menu()
    
