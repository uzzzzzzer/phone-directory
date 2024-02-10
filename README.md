# Phone Directory Program Documentation

## Introduction
The Phone Directory Program is a console-based application that allows users to manage a directory of contacts. Users can add, edit, search, and display entries in the directory.

## Features
1. Display Entries: View entries in the directory page by page.
2. Add Entry: Add a new contact entry to the directory.
3. Edit Entry: Modify an existing contact entry in the directory.
4. Search Entries: Search for contacts by one or more characteristics.

## Implementation Details
- **Programming Language:** Python
- **User Interface:** Console-based (no graphical interface)
- **Data Storage:** Text file (`phone_directory.txt`)
- **Regex Validation:** Fields are validated against predefined regex patterns to ensure data integrity.

## File Structure
- `phone_directory.py`: Main program file containing the implementation of the phone directory functionality.
- `phone_directory.txt`: Text file storing the directory data.

## Functionality Details
### 1. Display Entries
- Users can view entries in the directory page by page.
- They can specify the page size and page number to navigate through the entries.

### 2. Add Entry
- Users can add a new contact entry to the directory.
- The program prompts users to enter the following details:
  - Surname
  - First Name
  - Patronymic
  - Organization
  - Work Phone
  - Personal Phone
- Input values are validated against regex patterns to ensure data integrity.

### 3. Edit Entry
- Users can modify an existing contact entry in the directory.
- They specify the index of the entry they want to edit.
- For each field of the entry, users have the option to leave it blank to keep the current value.
- Input values are validated against regex patterns to ensure data integrity.

### 4. Search Entries
- Users can search for contacts by providing substrings for each characteristic (surname, first name, etc.).
- The program displays matching entries based on the provided search criteria.

## Usage
1. Run the `phone_directory.py` file.
2. Choose an option from the menu:
   - Display Entries (Option 1)
   - Add Entry (Option 2)
   - Edit Entry (Option 3)
   - Search Entries (Option 4)
   - Exit (Option 5)

## Dependencies
- Python 3.x

## How to Run
1. Ensure Python is installed on your system.
2. Download or clone the repository containing the `phone_directory.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `phone_directory.py` file.
5. Run the program by executing the command: `python phone_directory.py`.

## Example
Here's an example of how to use the program:
```
Phone Directory Menu:
1. Display Entries
2. Add Entry
3. Edit Entry
4. Search Entries
5. Exit
Enter your choice: 2
Enter surname: Smith
Enter name: John
Enter patronymic: Robertson
Enter organization: XYZ Corp
Enter work_phone: +79384092985
Enter personal_phone: 83049384920
Entry added successfully.

Phone Directory Menu:
1. Display Entries
2. Add Entry
3. Edit Entry
4. Search Entries
5. Exit
Enter your choice: 1
Enter page size: 2
Enter page number: 1
Smith, John, Robertson, XYZ Corp, +79384092985, 83049384920

Phone Directory Menu:
1. Display Entries
2. Add Entry
3. Edit Entry
4. Search Entries
5. Exit
Enter your choice: 3
Enter index of the entry to edit: 0
Enter surname replacement (leave blank to keep the current value): Taylor
Enter name replacement (leave blank to keep the current value): 
Enter patronymic replacement (leave blank to keep the current value): 
Enter organization replacement (leave blank to keep the current value): ZYX Corp
Enter work_phone replacement (leave blank to keep the current value): 
Enter personal_phone replacement (leave blank to keep the current value): 
Entry edited successfully.

Phone Directory Menu:
1. Display Entries
2. Add Entry
3. Edit Entry
4. Search Entries
5. Exit
Enter your choice: 4
Enter surname substring: 
Enter first name substring: 
Enter patronymic substring: 
Enter organization substring: Corp
Enter work phone substring: 0
Enter personal phone substring: 
Search results:
Taylor, John, Robertson, ZYX Corp, +79384092985, 83049384920

Phone Directory Menu:
1. Display Entries
2. Add Entry
3. Edit Entry
4. Search Entries
5. Exit
Enter your choice: 5
Exiting the program.
```

