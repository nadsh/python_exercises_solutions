# Important thing:
# This is an exercise in handling input. Be creative, solution doesn't matter.
product_cost = float(input("Product cost: "))
location = input("Location: ")

location_lower = location.lower()
if location_lower == 'canada':
    shipping = 3
elif location_lower in ('us', 'united states', 'america'):
    shipping = 5
elif location_lower in ('europe', 'united kingdom', 'uk', 'england', 'scotland', 'ireland', 'idklol'):
    shipping = 7
else:
    shipping = 9

print(f"You have to pay {product_cost + shipping}$, {product_cost}$ for the product and {shipping}$ for shipping to {location}.")