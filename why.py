#These are variable we are declaring
unit = input(f"Enter the unit of temperature (C/K): ").upper()
Degree = float(input(f"Enter the degree: "))

#This is if statement and logic part
if unit == "C":
    results = Degree + 273
    print(f"Your conversion is {results} K")
elif unit == "K":
    results = Degree -273
    print(f"Your conversion is {results} degrees celsius")
else:
    print(f"Your units are invalid")

#This was the first program this year

print(f"you are in the end of program congratulations")
