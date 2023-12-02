# Important thing:
# * Using %10 is the intended solution, but it works uniquely for negative numbers.
#   (-6 % 10) == 4
number = int(input())

# Option 1 - convert to string and access first character from the end.
print(str(number)[-1])
# Option 2 - convert to string and access character at "length-1" (last character).
print(str(number)[len(str(number))-1])

# The function "abs" turns a negative number to positive. abs(X) == abs(-X)

# Option 3 - get the absolute value of the number (google) then use %10
print(abs(number) % 10)

# Option 4 - do the work of "abs" manually then use % 10.
print(
    (number % 10) 
    if (number >= 0)
    else ((-number) % 10)
)

# Option 5 - use %10 then fix the value if the number was negative
print(
    number % 10
    if number >= 0
    else 10 - (number % 10)
)