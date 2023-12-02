# Important thing:
# * Decide on a rule of whether it's allowed to buy non-whole amounts of coins (0.5 bitcoin).
#   No matter how you choose to solve this, you must make an informed decision.
# * If you want, make sure that all user inputs are positive numbers.
total_money = float(input("How much money do you have? "))
assert total_money >= 0
bitcoin_price = float(input("Price of bitcoin? "))
assert bitcoin_price > 0
ethereum_price = float(input("Price of ethereum? "))
assert ethereum_price > 0
litecoin_price = float(input("Price of litecoin? "))
assert litecoin_price > 0

# Solution for whole numbers only. Operator // means divie into whole numbers.
print(f"Can buy {total_money // bitcoin_price} bitcoin.")
print(f"Can buy {total_money // ethereum_price} ether.")
print(f"Can buy {total_money // litecoin_price} lite.")

# Solution for fractions
print(f"Can buy {total_money / bitcoin_price} bitcoin.")
print(f"Can buy {total_money / ethereum_price} ether.")
print(f"Can buy {total_money / litecoin_price} lite.")