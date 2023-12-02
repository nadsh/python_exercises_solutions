# Important thing:
# * when swapping values, don't override one with the other.
a = float(input("Give number: "))
b = float(input("Give other number: "))
temp = a
a = b
b = temp
print(f"Switched values: {a}, {b}")
# another solution that works: 
# a, b = b, a