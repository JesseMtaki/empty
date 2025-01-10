unit = input(f"Enter the unit of temperature (C/K): ").upper()
Degree = float(input(f"Enter the degree: "))

if unit == "C":
    results = Degree + 273
    print(f"Your conversion is {results} K")
elif unit == "K":
    results = Degree -273
    print(f"Your conversion is {results} degrees celsius")
else:
    print(f"Your units are invalid")




