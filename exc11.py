# Important things:
# * round down numbers using int() or math.floor() or //. I will give examples for all.
import math

hours_worked = int(input("How many hours? "))
income = float(input("hourly income? "))
money = hours_worked * income

print(f"Can get {money // 200} PS4 consoles.")
print(f"Can get {math.floor(money / 900)} phones.")
print(f"Can get {int(money / 500)} TVs.")
print(f"Can get {money // 9.99} skins.")