"""
Studnet Name: Chandreshkumar Pravinbhai Patel
Student ID: 100925696

This is a for Final Test of Scripting. 
Test Time: 12:10 to 2:00

"""

import json

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def is_positive_integer(value):
    return value.isdigit() and int(value) > 0

def is_not_empty(value):
    return bool(value.strip())

virtual_machines = []

while True:
    print("\nEnter details for a new virtual machine:")
    
    name = get_valid_input("Enter VM name: ", is_not_empty)
    cpu = int(get_valid_input("Enter number of CPUs: ", is_positive_integer))
    memory = int(get_valid_input("Enter amount of memory in GB: ", is_positive_integer))
    bandwidth = get_valid_input("Enter description of bandwidth: ", is_not_empty)

    vm = {
        "name": name,
        "cpu": cpu,
        "memory": memory,
        "bandwidth": bandwidth
    }

    virtual_machines.append(vm)

    add_more = input("Do you want to add another virtual machine? (yes/no): ").lower()
    if add_more != 'yes':
        break

# Save the list of virtual machines to a JSON file
filename = "Chandreshkumar Test Result.json"
with open(filename, 'w') as f:
    json.dump(virtual_machines, f, indent=2)

print(f"\nVirtual machines data has been saved to {filename}")





