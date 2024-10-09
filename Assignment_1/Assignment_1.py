"""
Assignment 1
Perform by : Chandreshkumar Patel (100925696)

Selected Option: 1 (Check for prime number and it's related functions).
"""


# Function to Check if a Number is Prime

def is_prime(n):
    """
    Checks if a number is prime.

    Returns:
        True if the number is prime, False otherwise.

    This function is checking for prime number, if given number is prime, it give true, otherwise false.    
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to Find Previous and Next Prime Numbers

def previous_prime(n):
    """
    Finds the previous prime number.

    Returns:
        int: The previous prime number, or None if not found.

    This function is checking for previous prime number, if given number is prime then it function gives a previous prime number.    
    """
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None

def next_prime(n):
    """
    Finds the next prime number.

    Returns:
        int: The next prime number.

    This function is for next prime, if given number is prime, it gives next possible prime number.
    """
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1

# Function to Find Divisors

def find_divisors(n):
    """
    Finds the divisors of a number.

    Returns:
        list: A list of divisors.

    This function is for divisor, if given number is not a prime number, it gives a divisors of given number.    
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Main Application

def main():
    while True:
        user_input = input("Please enter the number to check: ") # Taking number from the user
        try:
            num = int(user_input)
            if num <= 0:
                print("That is not a positive whole number. Try again.") # if the input is not a number, it will execute.
                continue
            break
        except ValueError:
            print("That is not a positive whole number. Try again.") #if input is not a number, it is an error and program starts again.

    prev_prime = previous_prime(num) # if input is a number, this function search for previous prime number.
    if prev_prime is not None:
        print(f"The prime number before {num} is {prev_prime}.") # it gives previous prime number.
    else:
        print(f"There is no prime number before {num}.") # it will execute if there is no previous prime number.

    if is_prime(num): # it checks if number is prime or not.
        print(f"{num} is a prime number.") # if prime this is a output.
    else:
        print(f"{num} is not a prime number.") # if not this is a output.
        divisors = find_divisors(num) # if number is not a prime then it find the divisors of given number. (if number is prime, it will not execute).
        print(f"The divisors of {num} are: {divisors}") # output of divisors.

    next_prime_num = next_prime(num) # it find the next prime number of given number.(Doesn't matter number is prime or not).
    print(f"The prime number after {num} is {next_prime_num}.") # next prime number

    input("Press Enter to exit the program...")

if __name__ == "__main__":
    main()


"""
Referances:
    https://www.programiz.com/python-programming/examples/prime-number
    https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
    https://stackoverflow.com/questions/69423838/next-prime-number-in-python
    https://www.tutorialgateway.org/python-program-to-find-all-divisors-of-an-integer/
    https://alexwlchan.net/2019/finding-divisors-with-python/
    https://www.geeksforgeeks.org/find-all-factors-of-a-natural-number/
    
"""