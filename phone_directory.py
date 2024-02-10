import os
import re

# Define the filename for storing directory data
DIRECTORY_FILE = "phone_directory.txt"

# Define regex patterns for each field
surname_pattern = r'^[A-Za-zА-Яа-я\s-]*$'
name_pattern = r'^[A-Za-zА-Яа-я\s]*$'
organization_pattern = r'^[A-Za-zА-Яа-я\s-]*$'
phone_pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

field_names = ["surname", "name", "patronymic", "organization", "work_phone", "personal_phone"]
field_patterns = [surname_pattern, name_pattern, name_pattern, organization_pattern, phone_pattern, phone_pattern]

def display_entries(page_size, page_number):
    """
    Display page-by-page entries from the directory on the screen.

    Args:
        page_size (int): Number of entries to display per page.
        page_number (int): Page number to display.
    """
    with open(DIRECTORY_FILE, 'r') as file:
        entries = file.readlines()
        start_index = (page_number - 1) * page_size
        end_index = min(start_index + page_size, len(entries))
        for i in range(start_index, end_index):
            print(entries[i].strip())

def add_entry(entry):
    """
    Add a new entry to the directory.

    Args:
        entry (str): Entry to add to the directory.
    """
    with open(DIRECTORY_FILE, 'a') as file:
        file.write(entry + '\n')

def edit_entry(index, new_entry):
    """
    Edit an entry in the directory.

    Args:
        index (int): Index of the entry to edit.
        new_entry (str): New entry to replace the existing one.
    """
    entries = []
    with open(DIRECTORY_FILE, 'r') as file:
        entries = file.readlines()
    if 0 <= index < len(entries):
        entries[index] = new_entry + '\n'
        with open(DIRECTORY_FILE, 'w') as file:
            file.writelines(entries)
        print("Entry edited successfully.")
    else:
        print("Invalid entry index.")

def search_entries():
    """
    Search for records by one or more characteristics.
    """
    surname = input("Enter surname substring: ")
    name = input("Enter first name substring: ")
    patronymic = input("Enter patronymic substring: ")
    organization = input("Enter organization substring: ")
    work_phone = input("Enter work phone substring: ")
    personal_phone = input("Enter personal phone substring: ")

    search_criteria = [surname.lower(), name.lower(), patronymic.lower(), organization.lower(), work_phone.lower(), personal_phone.lower()]

    with open(DIRECTORY_FILE, 'r') as file:
        entries = file.readlines()
        found_entries = []
        for entry in entries:
            fields = entry.strip().lower().split(', ')
            if all(criteria in field for criteria, field in zip(search_criteria, fields)):
                found_entries.append(entry.strip())

        if found_entries:
            print("Search results:")
            for entry in found_entries:
                print(entry)
        else:
            print("No matching entries found.")

def validate_fields(field_values):
    """
    Validate user input for each field against its corresponding regex pattern.

    Args:
        field_values (list): List of field values to validate.

    Returns:
        bool: True if all fields match their patterns, False otherwise.
    """
    return all(re.match(pattern, value) is not None for pattern, value in zip(field_patterns, field_values))

def main():
    # Create the directory file if it doesn't exist
    if not os.path.exists(DIRECTORY_FILE):
        open(DIRECTORY_FILE, 'a').close()

    while True:
        print("\nPhone Directory Menu:")
        print("1. Display Entries")
        print("2. Add Entry")
        print("3. Edit Entry")
        print("4. Search Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            page_size = int(input("Enter page size: "))
            page_number = int(input("Enter page number: "))
            display_entries(page_size, page_number)
        elif choice == '2':
            field_values = []
            for field in field_names:
                value = input(f"Enter {field}: ")
                field_values.append(value)
            if validate_fields(field_values):
                entry = ", ".join(field_values)
                add_entry(entry)
                print("Entry added successfully.")
            else:
                print("Invalid input format.")
        elif choice == '3':
            index = int(input("Enter index of the entry to edit: "))
            current_entry = ""
            with open(DIRECTORY_FILE, 'r') as file:
                entries = file.readlines()
                if 0 <= index < len(entries):
                    current_entry = entries[index].strip()
                else:
                    print("Invalid entry index.")
                    continue
            edited_fields = []
            field_values = current_entry.split(', ')
            for old_value, field in zip(field_values, field_names):
                new_value = input(f"Enter {field} replacement (leave blank to keep the current value): ")
                edited_fields.append(old_value if new_value == "" else new_value)
            if validate_fields(edited_fields):
                new_entry = ", ".join(edited_fields)
                edit_entry(index, new_entry)
            else:
                print("Invalid input format.")
        elif choice == '4':
            search_entries()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
