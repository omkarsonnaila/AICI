unit = input("Convert from (C/F): ").strip().upper()
temp = float(input("Enter temperature: "))

if unit == "C":
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result:.2f}°F")
elif unit == "F":
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.2f}°C")
else:
    print("Invalid unit. Use 'C' or 'F'.")
