# IT Ticket Management System
A Python command-line application that allows users to create, manage, search, and track IT support tickets. The application will simulate a basic IT help desk ticketing system.

## Features ##

- Create - Record new IT support requests
- View - Display all existing tickets
- Search - Search by ticket ID
- Update - Change ticket information
- Assign - Assign tickets to technicians
- Close - Change ticket status
- Filter - Filter by priority or status
- Save/Load - Store tickets in JSON
- Backup/Recovery - Create backup copies and restore tickets if the primary data file is unavailable

## Ticket Information

Each ticket will contain:
- Ticket ID
- Title
- Description
- Priority (Low, Medium, High, Critical)
- Status (Open, In Progress, Resolved, Closed)
- Assigned Technician

## Technologies Used

- Python 3
- JSON -  Data storage and persistence
- shutil - Backup file creation and recovery

## How To Use

- Clone or download the repository
  - `git clone https://github.com/Firehawk252/it-ticket-management-system.git`
- Navigate to the project directory
  - `cd it-ticket-management-system`
- Run the application
  - `python main.py`