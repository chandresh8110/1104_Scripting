'''
Student Name: Chandreshkumar Pravinbhai Patel
Student ID: 100925696

This file is for Practical Mid Exam in Scripting from 12:51 to 1:51.

'''
#Constants
TOTAL_SERVERS = 3
MAX_ACCOUNTS = 50

# Asking user for inputs
server_1_accounts = int(input("Enter the number of accounts for Server 1: "))
server_2_accounts = int(input("Enter the number of accounts for Server 2: "))

# Calculating total accounts assigned to the first two servers
total_account = server_1_accounts + server_2_accounts

# Checking if the total acconts are exceeds or equals the maximum allowed accounts
if total_account > MAX_ACCOUNTS:
    print("You have exceeded the maximum allowable accounts.")
    remaining_accounts = 0  # No remaining accounts for Server 3
elif total_account == MAX_ACCOUNTS:
    print("There are no additional accounts allowed.")
    remaining_accounts = 0  # No remaining accounts for Server 3
else:
    remaining_accounts = MAX_ACCOUNTS - total_account
    print(f"There are {remaining_accounts} accounts still available.")

# Display the accounts for each server
print("Server 1 Accounts:", server_1_accounts)
print("Server 2 Accounts:", server_2_accounts)
print("Server 3 Accounts:", remaining_accounts)

# Loop for exit
exit_program = input("Do you want to exit the program? (yes/no): ").lower()

while exit_program != "yes":
    exit_program = input("Do you want to exit the program? (yes/no): ").lower()


print("Exiting the program.")

