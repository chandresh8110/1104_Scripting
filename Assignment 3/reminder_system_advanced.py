"""
Student Name: Chandreshkumar Pravinbhai Patel
Student Id: 100925696

This is an assignment 3 for Scripting.

"""

import time
from datetime import datetime
from plyer import notification

REMINDER_FILE = "reminders.txt"

def add_reminder():
    """Add a new reminder."""
    description = input("Enter the reminder description: ")
    reminder_time = input("Enter the reminder time (YYYY-MM-DD HH:MM): ")
    
    with open(REMINDER_FILE, "a") as file:
        file.write(f"{description}|{reminder_time}\n")
    
    print("Reminder added successfully!")

def check_reminders():
    """Check for due reminders and send notifications."""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")

    with open(REMINDER_FILE, "r") as file:
        reminders = file.readlines()

    for reminder in reminders:
        description, reminder_time = reminder.strip().split('|')
        if reminder_time == current_time:
            send_notification(description)

def send_notification(message):
    """Send a notification."""
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10
    )
    print(f"Notification sent: {message}")

def main():
    """Main loop for the reminder system."""
    while True:
        print("\n1. Add Reminder")
        print("2. Check Reminders")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_reminder()
        elif choice == '2':
            check_reminders()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(10)  # Check reminders every minute

if __name__ == "__main__":
    main()