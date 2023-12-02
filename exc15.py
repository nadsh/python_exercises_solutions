# Be very careful not to count the same second for multiple different rates.
# Some answers:
#   100s = 26$      (25+1)
#   500s = 30$      (25+5)
#   600s = 30.8$    (25 + 5 + 0.8)
#   800s = 32.4$    (25 + 5 + 2.4)
#   1000s = 33.4$   (25 + 5 + 2.4 + 1)
seconds = int(input('seconds: '))
base_rate = 25 
rate1 = 0.01 * min(seconds, 500)

if seconds > 500:
    rate2 = 0.008 * min(seconds - 500, 300)
else:
    rate2 = 0

if seconds > 800:
    rate3 = 0.005 * (seconds - 800)
else:
    rate3 = 0


bill = base_rate + rate1 + rate2 + rate3

print(f"The bill is {bill}")