"""
Student Name: Chandreshkumar Pravinbhai Patel
Student Id: 100925696

This is an assignment 3 for Scripting.

"""


import time
from datetime import datetime
import os
import winsound  # For sound notifications (Windows)
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

REMINDER_FILE = "reminders.txt"

def add_reminder():
    """Add a new reminder with date and time validation."""
    description = input("Enter the reminder description: ")

    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD.")

    while True:
        time_input = input("Enter the time (HH:MM, 24-hour format): ")
        try:
            datetime.strptime(time_input, "%H:%M")
            break
        except ValueError:
            print(Fore.RED + "Invalid time format. Please use HH:MM.")

    with open(REMINDER_FILE, "a") as file:
        file.write(f"{description}|{date}|{time_input}\n")

    print(Fore.GREEN + "Reminder added successfully!\n")

def view_reminders():
    """Display all saved reminders."""
    print(Fore.CYAN + "\nUpcoming Reminders:")
    if not os.path.exists(REMINDER_FILE):
        print(Fore.YELLOW + "No reminders found.")
        return

    with open(REMINDER_FILE, "r") as file:
        reminders = file.readlines()
        if reminders:
            for reminder in reminders:
                description, date, time = reminder.strip().split('|')
                print(Fore.LIGHTBLUE_EX + f"- {description} on {date} at {time}")
        else:
            print(Fore.YELLOW + "No reminders found.")
    print()

def check_reminders():
    """Check if any reminder matches the current date and time and trigger a notification."""
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")

    if not os.path.exists(REMINDER_FILE):
        return

    with open(REMINDER_FILE, "r") as file:
        reminders = file.readlines()

    with open(REMINDER_FILE, "w") as file:  # Rewrite file without triggered reminders
        for reminder in reminders:
            description, date, time = reminder.strip().split('|')
            if date == current_date and time == current_time:
                print(Fore.MAGENTA + f"\n⏰ Reminder: {description} now!")
                play_sound()
            else:
                file.write(reminder)

def play_sound():
    """Play a sound notification when a reminder is triggered."""
    frequency = 1000  # Frequency in Hz
    duration = 500    # Duration in ms
    winsound.Beep(frequency, duration)

def main():
    """Main function to run the reminder system."""
    while True:
        print(Fore.YELLOW + "1. Add a Reminder")
        print(Fore.YELLOW + "2. View Reminders")
        print(Fore.YELLOW + "3. Exit\n")

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == '1':
            add_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.\n")

        print(Fore.CYAN + "Checking reminders...")
        check_reminders()
        time.sleep(60)  # Wait for 60 seconds before checking reminders again

if __name__ == "__main__":
    main()
