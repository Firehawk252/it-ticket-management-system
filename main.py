# IT Ticket Management System
# A command-line application for users to create, manage, search, and track IT support tickets
# Firehawk252 11/10/2026
# v.1.0

import json
import shutil

# Create a save tickets function
# Every time tickets are saved, create a backup copy of tickets.json named tickets_backup.json
def save_tickets(tickets):
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

    shutil.copy("tickets.json", "tickets_backup.json")

    print("Tickets saved successfully!")
    print("Backup created successfully!")

# Create a load tickets function
def load_tickets():
    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)
            return tickets
    except FileNotFoundError:
        try:
            with open("tickets_backup.json", "r") as file:
                tickets = json.load(file)
                print("Tickets restored from backup!")
                return tickets
        except FileNotFoundError:
            print("No tickets or backup file found.")
            return []

# Create tickets
def create_ticket(tickets):
    while True:
        ticket_id = input("Enter Ticket ID: ")
        if ticket_id == "":
            print("Ticket ID cannot be empty.")
            continue
        else:
            found = False
            for ticket in tickets:
                if ticket["Ticket ID"] == ticket_id:
                    found = True
                    print("Ticket ID already exists.")
                    break
            if found:
                continue
            else:
                break

    while True:
        title = input("Enter Ticket Title: ")
        if title == "":
            print("Ticket Title cannot be empty.")
            continue
        else:
            found = False
            for ticket in tickets:
                if ticket["Title"] == title:
                    found = True
                    print("Ticket Title already exists.")
                    break
            if found:
                continue
            else:
                break

    while True:
        desc = input("Enter Ticket Description: ")
        if desc == "":
            print("Ticket Description cannot be empty.")
            continue
        else:
            break
    while True:
        prio = input("Enter Priority (i.e., Low, Medium, High, Critical): ").lower()
        if prio == "":
            print("Priority cannot be empty.")
            continue
        elif prio not in ["low", "medium", "high", "critical"]:
            print("Invalid Priority. Priority must be 'Low', 'Medium', 'High', 'Critical'.")
            continue
        else:
            break

    while True:
        stat = input("Enter Ticket Status (i.e., Open, In Progress, Resolved, Closed): ").lower()
        if stat == "":
            print("Ticket Status cannot be empty.")
            continue
        elif stat not in ["open", "in progress", "resolved", "closed"]:
            print("Invalid Status. Status must be 'Open', 'In Progress', 'Resolved', 'Closed'.")
            continue
        else:
            break

    while True:
        tech = input("Enter Assigned Technician: ")
        if tech == "":
            print("Assigned Technician cannot be empty.")
            continue
        else:
            break
    ticket = {
        "Ticket ID": ticket_id,
        "Title": title,
        "Description": desc,
        "Priority": prio,
        "Status": stat,
        "Assigned Technician": tech
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print("Ticket Created Successfully!")

# View tickets
def view_tickets(tickets):
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            print("Ticket ID", ticket["Ticket ID"])
            print("Title", ticket["Title"])
            print("Description", ticket["Description"])
            print("Priority", ticket["Priority"])
            print("Status", ticket["Status"])
            print("Assigned Technician", ticket["Assigned Technician"])
            print("---------------------------")
        print("Total Number of Tickets: ", len(tickets), "\n")

# Search tickets
def search_tickets(tickets):
    user_input = input("Enter Ticket ID: ")
    found = False
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            if user_input == ticket["Ticket ID"]:
                found = True
                print("Ticket ID", ticket["Ticket ID"])
                print("Title", ticket["Title"])
                print("Description", ticket["Description"])
                print("Priority", ticket["Priority"])
                print("Status", ticket["Status"])
                print("Assigned Technician", ticket["Assigned Technician"])
        if not found:
            print("Ticket not found.")

# Update tickets
def update_ticket(tickets):
    user_input = input("Enter Ticket ID: ")
    found = False
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            if user_input == ticket["Ticket ID"]:
                found = True
                while True:
                    print("1. Update Title")
                    print("2. Update Description")
                    print("3. Update Priority")
                    print("4. Update Status")
                    print("5. Return to Main Menu")

                    try:
                        choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid Choice.")
                        continue

                    if choice == 1:
                        while True:
                            title = input("Enter new Title: ")
                            if title == "":
                                print("Ticket Title cannot be empty.")
                                continue
                            else:
                                found = False
                                for other_ticket in tickets:
                                    if other_ticket != ticket and other_ticket["Title"] == title:
                                        found = True
                                        print("Ticket Title already exists.")
                                        break
                                if found:
                                    continue
                                else:
                                    ticket["Title"] = title
                                    break
                        save_tickets(tickets)
                        print("Ticket updated successfully!")

                    elif choice == 2:
                        while True:
                            desc = input("Enter new Description: ")
                            if desc == "":
                                print("Ticket Description cannot be empty.")
                                continue
                            else:
                                ticket["Description"] = desc
                                save_tickets(tickets)
                                print("Ticket updated successfully!")
                                break

                    elif choice == 3:
                        while True:
                            prio = input("Enter new Priority: ").lower()
                            if prio == "":
                                print("Ticket Priority cannot be empty.")
                                continue
                            elif prio not in ["low", "medium", "high", "critical"]:
                                print("Invalid Priority. Priority must be 'low', 'medium', 'high, or 'critical'.")
                                continue
                            else:
                                ticket["Priority"] = prio
                                save_tickets(tickets)
                                print("Ticket updated successfully!")
                                break

                    elif choice == 4:
                        while True:
                            stat = input("Enter new Status: ").lower()
                            if stat == "":
                                print("Ticket Status cannot be empty.")
                                continue
                            elif stat not in ["open", "in progress", "resolved", "closed"]:
                                print("Invalid Status. Status must be 'open', 'in progress', 'resolved' or 'closed'.")
                                continue
                            else:
                                ticket["Status"] = stat
                                save_tickets(tickets)
                                print("Ticket updated successfully!")
                                break

                    elif choice == 5:
                        break

                    else:
                        print("Invalid Choice.")
        if not found:
            print("Ticket not found.")

# Assign tickets
def assign_ticket(tickets):
    user_input = input("Enter Ticket ID: ")
    found = False
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            if user_input == ticket["Ticket ID"]:
                found = True
                print("Current Assigned Technician", ticket["Assigned Technician"])
                new_tech = input("Would you like to update the assigned technician (y/n)? ").lower()
                if new_tech == "y":
                    ticket["Assigned Technician"] = input("Enter new Technician: ")
                    save_tickets(tickets)
                    print("Ticket assigned successfully!")
                elif new_tech == "n":
                    break
                else:
                    print("Invalid Choice.")
        if not found:
            print("Ticket not found.")

# Close tickets
def close_ticket(tickets):
    user_input = input("Enter Ticket ID: ")
    found = False
    if not tickets:
        print("No tickets found.")
    else:
        for ticket in tickets:
            if user_input == ticket["Ticket ID"]:
                found = True
                print("Current Status: ", ticket["Status"])
                new_status = input("Would you like to close the ticket (y/n)? ").lower()
                if new_status == "y":
                    ticket["Status"] = "Closed"
                    save_tickets(tickets)
                    print("Ticket closed successfully!")
                elif new_status == "n":
                    break
                else:
                    print("Invalid Choice.")
        if not found:
            print("Ticket not found.")

# Filter tickets
def filter_tickets(tickets):
    found = False
    count = 0
    if not tickets:
        print("No tickets found.")
    else:
        print("1. Filter by Priority")
        print("2. Filter by Status")
        print("3. Return to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_prio = input("Enter a Priority (Low, Medium, High, Critical): ").lower()
            for ticket in tickets:
                if user_prio == ticket["Priority"].lower():
                    found = True
                    count += 1
                    print("Ticket ID: ", ticket["Ticket ID"])
                    print("Title: ", ticket["Title"])
                    print("Description: ", ticket["Description"])
                    print("Priority: ", ticket["Priority"])
                    print("Status: ", ticket["Status"])
                    print("Assigned Technician: ", ticket["Assigned Technician"])
                    print("---------------------------")
            if not found:
                print("No matching tickets found.")
            else:
                print("Total Number of", user_prio.title(), "Tickets:", count, "\n")

        elif choice == 2:
            user_stat = input("Enter a Status (Open, In Progress, Resolved, Closed): ").lower()
            for ticket in tickets:
                if user_stat == ticket["Status"].lower():
                    found = True
                    count += 1
                    print("Ticket ID: ", ticket["Ticket ID"])
                    print("Title: ", ticket["Title"])
                    print("Description: ", ticket["Description"])
                    print("Priority: ", ticket["Priority"])
                    print("Status: ", ticket["Status"])
                    print("Assigned Technician: ", ticket["Assigned Technician"])
                    print("---------------------------")
            if not found:
                print("No matching tickets found.")
            else:
                print("Total Number of", user_stat.title(), "Tickets:", count, "\n")

        elif choice == 3:
            return
        else:
            print("Invalid Choice.")

def main():

    tickets = load_tickets()

    print("==============================")
    print("     IT Ticket Management")
    print("==============================")

    while True:
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Search Tickets")
        print("4. Update Ticket")
        print("5. Assign Ticket")
        print("6. Close Ticket")
        print("7. Filter Tickets")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice.")
            continue

        if choice == 1:
            create_ticket(tickets)

        elif choice == 2:
            view_tickets(tickets)

        elif choice == 3:
            search_tickets(tickets)

        elif choice == 4:
            update_ticket(tickets)

        elif choice == 5:
            assign_ticket(tickets)

        elif choice == 6:
            close_ticket(tickets)

        elif choice == 7:
            filter_tickets(tickets)

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid Choice.")




main ()