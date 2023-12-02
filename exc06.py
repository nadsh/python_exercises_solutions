# Important thing
# User input should be a positive number and then a non-negative number to make sense.
price = float(input("Laptop price: "))
assert price > 0
tax_percent = float(input("tax %: "))
assert tax_percent >= 0

tax_in_dollars = tax_percent * price / 100
print(f"The total price of the laptop is {price + tax_in_dollars}$")