# Important things:
# * Support negative percentage for decreases (-10)
# * If you want, check that the decrease is not lower than -100.
    
initial_value = float(input("What was the initial bitcoin value?"))
# Keep in mind: input of 10 is 10% increase, input of -20 is 20% decrease
perc = float(input("What was the percentage increase?")) 

diff = initial_value * perc / 100
new_value = initial_value + diff

print(f'total_bitcoin_value = {new_value}, bitcoin_increase_value = {diff}')