"""
THIS IS A INCLASS-3 ACTIVITY.
PERFORM BY CHANDRESHKUMAR PATEL (100925696).
GROUP NO 11. 

TO PERFORM THIS ACTIVITY, I TOOK A HELP FROM WEB-SITE NAMED W3SCHOOL, GREEKFORGREEK AND JAVATPOINT. HERE I AM REFERENCING IT.
https://www.w3schools.com/python/python_comments.asp
https://www.geeksforgeeks.org/python-program-for-sum-the-digits-of-a-given-number/
https://www.geeksforgeeks.org/program-remove-vowels-string/ 

"""

#Returns TRUE if the input number is a power of 2, otherwise FALSE.
def is_power_of_two(number: int) -> bool:
    if number <= 0:
        return False
    return (number & (number - 1)) == 0


#Returns the SUM of the individual digits of the input number IN STRING.
def sum_of_digits(number: int) -> int:
    return sum(int(digit) for digit in str(number))


#Returns the input string with ALL REMOVED VOWELS.
def rem_vowels(s: str) -> str:
    vowels = 'aeiouAEIOU'
    return ''.join(c for c in s if c not in vowels)

def main():
    
#This will check that the given number is power of two or not?
    print("\nTesting is_power_of_two()...")
    print(f"Is 8 a power of two? {is_power_of_two(8)}")
    print(f"Is 10 a power of two? {is_power_of_two(10)}")
    print(f"Is 16 a power of two? {is_power_of_two(16)}")

#This will doing the sum of given digites.
    print("\nTesting sum_of_digits()...")
    print(f"The sum of the digits of 123 is {sum_of_digits(123)}")
    print(f"The sum of the digits of 456 is {sum_of_digits(456)}")
    print(f"The sum of the digits of 789 is {sum_of_digits(789)}")

#This will remove the vowels from the given string.
    print("\nTesting rem_vowels()...")
    print(f"'hello world' without vowels is '{rem_vowels('hello world')}'")
    print(f"'The quick brown fox' without vowels is '{rem_vowels('The quick brown fox')}'")
    print(f"'AEIOU' without vowels is '{rem_vowels('AEIOU')}'")


if __name__ == "__main__":
    main()