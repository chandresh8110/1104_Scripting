"""
Assignment 2

Perform by : Chandreshkumar Patel (100925696)

Selected Problem: Time Tracking Tool
"""


import json
import os
from datetime import datetime

# File to store time tracking data
data_file = 'time_tracking.json'

# Load existing data or create a new one
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        time_data = json.load(file)
else:
    time_data = {}

def start_task(task_name):
    """Start tracking a new task."""
    start_time = datetime.now()
    time_data[task_name] = {'start_time': start_time.isoformat(), 'end_time': None}
    print(f"Started tracking task: '{task_name}' at {start_time.strftime ('%Y-%m-%d  %H:%M:%S')}")

def end_task(task_name):

    """End tracking a task."""
    if task_name in time_data and time_data[task_name]['end_time'] is None:
        end_time = datetime.now()
        time_data[task_name]['end_time'] = end_time.isoformat()
        print(f"Ended tracking task: '{task_name}' at {end_time.strftime ('%Y-%m-%d  %H:%M:%S')}")
    else:
        print(f"Task '{task_name}' is not currently being tracked or does not exist.")

def save_data():
    """Save time tracking data to a file."""
    with open(data_file, 'w') as file:
        json.dump(time_data, file, indent=4)
    print("Time tracking data saved.")

def view_report():
    """View the time tracking report."""
    print("\nTime Tracking Report:")
    for task, times in time_data.items():
        start_time = times['start_time']
        end_time = times['end_time'] if times['end_time'] else "Still running"
        print(f"Task: {task}, Start Time: {start_time}, End Time: {end_time}")

def main():
    while True:
        print("\nTime Tracking Tool")
        print("1. Start Task")
        print("2. End Task")
        print("3. View Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            start_task(task_name)
            save_data()
        elif choice == '2':
            task_name = input("Enter task name: ")
            end_task(task_name)
            save_data()
        elif choice == '3':
            view_report()
        elif choice == '4':
            print("Exiting the Time Tracking Tool.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()