def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    1 inch = 2.54 centimeters
    """
    return cm / 2.54

# Example usage
example_cm = 10
result = cm_to_inches(example_cm)
print(f"{example_cm} cm is equal to {result:.2f} inches.")