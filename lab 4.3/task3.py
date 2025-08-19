def generate_full_names():
    examples = []
    n = int(input("How many examples (2 or 3) do you want to enter? "))
    if n not in [2, 3]:
        print("Please enter 2 or 3 examples.")
        return
    for i in range(n):
        first = input(f"Enter first name for example {i+1}: ")
        last = input(f"Enter last name for example {i+1}: ")
        full_name = f"{last}, {first}"
        examples.append(full_name)
    print("Generated full names (Last, First):")
    for name in examples:
        print(name)

# Example usage:
generate_full_names()