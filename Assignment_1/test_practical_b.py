'''
Student Name: Chandreshkumar Pravinbhai Patel
Student ID: 100925696

This file is for Practical Mid Exam in Scripting from 12:51 to 1:51.

'''

Total_server = 3
Max_account = 50

def main():
    account_servers = [0] * Total_server
    while True:
        for i in range(Total_server):
            account_servers[i] = int(input(f"Enter the account for server {i+1}: "))

        total_account = sum(account_servers)

        if total_account > Max_account:
            print("You have exceeded the maximum allowable accounts.")
        elif total_account == Max_account:
            print("There are no additional accounts allowed.")
        else:
            remaining_account = Max_account - total_account
            print(f"There are {remaining_account} accounts still available.")

        for i in range(Total_server):
            print(f"Account for Server {i+1} = {account_servers[i]}")

        print(f"Remaining Available Accounts = {remaining_account}")

        exit_selection = input("Do you want to exit? (y/n): ").strip().lower()
        if exit_selection == 'y':
            break
        elif exit_selection != 'n':
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()