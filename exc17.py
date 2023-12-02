# The "range" function creates an "iterable".
# Example: list(range(start=3,stop=20,step=3)) == [3,6,9,12,15,18]
#          list(range(20)) = [1,2,3,4,5,...,18,19]
#          list (range(4,8)) = [4,5,6,7]
def sum_of_range_1(n):
    return (n*(n+1)) / 2

def sum_of_range_2(n):
    return sum(range(n+1))

def sum_of_range_3(n):
    s = 0
    for i in range(1, 100):
        s += i
    return s


print(sum_of_range_1(99))
print(sum_of_range_2(99))
print(sum_of_range_3(99))
