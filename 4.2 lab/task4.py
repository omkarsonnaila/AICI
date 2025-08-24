def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

num = input("Enter a number: ")
if num.isdigit():
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
else:
    print("Invalid input. Please enter a valid number.")