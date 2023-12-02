# Important things:
# * Be comfortable with the ternary expressions (a if b else c)
# * Try not to write the same code multiple times. You could have two separate prints, 
#   but my solution is better.

hours = int(input("How many hours "))

is_member_string = input("Is member? (yes/no)")
assert is_member_string in ("yes", "no")
is_member = "yes" if is_member_string == "yes" else "no"

rate, tax_multiplier = (2, 1.1) if is_member else (5, 1.2)
total = rate * hours * tax_multiplier

print(f"The user is {'a member' if is_member else 'not a member'}."
      f" Stayed {hours} hours for {2 if is_member else 5}$/hour plus the {10 if is_member else 20}%."
      f" The total amount is {total}$.")