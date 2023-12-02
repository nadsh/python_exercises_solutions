def average(a,b,c):
    return (a+b+c)/3

Geometry = float(input("Geometry grade:"))
Algebra =  float(input("Algebra grade:"))
Physics = float(input('Physics grade:'))
a = average(Geometry, Algebra, Physics)
if 10 >= a >= 7:
    feedback = "Good Job!"
elif 7 > a >= 4:
    feedback = "You need to work harder!"
elif 4 > a >= 0:
    feedback = "You suck!"
else:
    raise Exception(f'This average makes no sense. Your grades must not be between 0 and 10! {a}')

print(f'Your average score is {a}, {feedback}')