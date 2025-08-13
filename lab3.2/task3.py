# Example input-output pairs for convert_to_binary(num) function

# Example 1
# Input: 5
# Output: '101'

# Example 2
# Input: 12
# Output: '1100'

# Example 3
# Input: 0
# Output: '0'

# Example 4
# Input: 255
# Output: '11111111'

# Example 5
# Input: 1
# Output: '1'

def convert_to_binary(num):
    return bin(num)[2:]

# Take input from user and show output
num = int(input("Enter a number: "))
print("Binary representation:", convert_to_binary(num))