def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Example usage:
example_strings = [
    "Hello World",
    "Python Programming",
    "AIAS Lab"
]

for text in example_strings:
    print(f"'{text}' has {count_vowels(text)} vowels.")