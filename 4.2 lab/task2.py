#write a python function that converts farenheit to celcius
#example;
#input ;100
#output;37.78

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)

# Example usage:
f = 100
# Explanation:
# The function fahrenheit_to_celsius takes a temperature value in Fahrenheit as input.
# It converts this value to Celsius using the formula: (Fahrenheit - 32) * 5 / 9.
# The result is rounded to 2 decimal places using the round() function.
# In the example, f = 100 means 100 degrees Fahrenheit.
# The function returns 37.78, which is the equivalent temperature in Celsius.
