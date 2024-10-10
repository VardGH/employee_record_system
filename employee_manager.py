import csv

csv_file = "employees.csv"

def validate_name(enter_name):
    while True:
        name = input(enter_name).strip()
        if name.isalpha():
            return name
        else:
            print("\nInvalid name. Please enter only alphabetic characters.\n")

def validate_last_name(enter_last_name):
    while True:
        last_name = input(enter_last_name).strip()
        if last_name.isalpha():
            return last_name
        else:
            print("\nInvalid last name. Please enter only alphabetic characters.\n")

def validate_age(enter_age):
    while True:
        age = input(enter_age).strip()
        if age.isdigit() and 18 <= int(age) <= 100:
            return age
        else:
            print("\nInvalid age. Please enter a valid age between 18 and 100.\n")

def validate_department(enter_department):
    while True:
        department = input(enter_department).strip()
        if department.isalpha():
            return department
        else:
            print("\nInvalid department. Please enter only alphabetic characters.\n") 

def add_employee():
    name = validate_name("Enter your name: ")
    last_name = validate_last_name("Enter your last name: ")
    age = validate_age("Enter your age: ")
    department = validate_department("Enter your department: ")

    with open(csv_file, 'a') as file:
        write_in_csv = csv.writer(file)
        write_in_csv.writerow([name, last_name, age, department])

    print("\nEmployee added successfully.\n")


def view_all_employees():
    try:
        with open(csv_file, 'r') as file:
            read_in_csv = csv.reader(file)
            
            print(f"\n{'First Name':<15}{'Last Name':<15}{'Age':<10}{'Department':<15}")

            for row in read_in_csv:
                print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<15}")

            print()

    except FileNotFoundError:
        print("File does not exist yet.\n")

def search_employee_by_name():
    name = validate_name("Enter name to search: ").lower()
    is_exist = False

    try:
        with open(csv_file, 'r') as file:
            read_in_csv = csv.reader(file)
            print(f"\n{'First Name':<15}{'Last Name':<15}{'Age':<10}{'Department':<15}")
            
            for row in read_in_csv:
                if name == row[0].lower():
                    is_exist = True
                    print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<15}")
            
            if not is_exist:
                print("Employee not found.\n")
    except FileNotFoundError:
        print("File does not exist yet.\n")

def advanced_search():
    name = input("Enter name (leave blank if not searching by name): ").lower()
    last_name = input("Enter last name (leave blank if not searching by last name): ").lower()
    age = input("Enter age (leave blank if not searching by age): ")
    department = input("Enter department (leave blank if not searching by department): ").lower()

    is_exist = False

    try:
        with open(csv_file, 'r') as file:
            read_in_csv = csv.reader(file)
            print(f"\n{'First Name':<15}{'Last Name':<15}{'Age':<10}{'Department':<15}")
            print("-" * 55)

            for row in read_in_csv:
                if ((not name or name == row[0].lower()) and
                    (not last_name or last_name == row[1].lower()) and
                    (not age or age == row[2]) and
                    (not department or department == row[3].lower())):
                    is_exist = True
                    print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<15}")

            print()

            if not is_exist:
                print("Employee(s) not found\n")
    except FileNotFoundError:
        print("File does not exist yet.\n")

def main():
    while True:
        print("1. Add new employee.")
        print("2. View all employees.")
        print("3. Search employee by name. ")
        print("4. Advanced search. ")
        print("5. Exit.")

        input_choice = input("Please enter your chice(1-4): ")

        if input_choice == '1':
            add_employee()
        elif input_choice == '2':
            view_all_employees()
        elif input_choice == '3':
            search_employee_by_name()
        elif input_choice == '4':
            advanced_search()
        elif input_choice == '5':
            print("Exit!")
            break
        else:
            print("Youre input is wrong, please enter a number between 1 and 4.\n ")


if __name__ == "__main__":
    main()