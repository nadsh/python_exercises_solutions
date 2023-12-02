# Important things:
# * width and height must be positive numbers.
width = float(input("Width: "))
assert width > 0, f'It makes no sense that Width is this number: {width}'
height = float(input("Height: "))
assert height > 0, f'It makes no sense that Height is this number: {height}'

print(width * height)