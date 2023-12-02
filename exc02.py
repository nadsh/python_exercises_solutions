# Important things:
# * If you want, make sure that the grades are "legal" (between 0 and 10)
def average(a,b,c):
    return (a+b+c)/3

Geometry = float(input("Geometry grade:"))
assert 0 <= Geometry <= 10
Algebra =  float(input("Algebra grade:"))
assert 0 <= Algebra <= 10
Physics = float(input('Physics grade:'))
assert 0 <= Physics <= 10
print(average(Geometry, Algebra, Physics))