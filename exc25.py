# I decided to handle the possibility of bad input by just raising an exception.
heads = 0
tails = 0
total = 0
while True:
    flip_result = input("next flip: ")
    if flip_result not in ("head", "tails", "stop"):
        raise ValueError(f"Illegal flip result: {flip_result}")

    if flip_result == "stop":
        break
    
    total += 1
    if flip_result == "head":
        heads += 1
    if flip_result == "tails":
        tails += 1

print(f"Head won {heads} times and tails won {tails} times.")
heads_fraction = heads / total
heads_percentage = heads_fraction * 100
tails_percentage = 100 - heads_percentage
print(f"{heads_percentage}% Head, {tails_percentage}% Tails")