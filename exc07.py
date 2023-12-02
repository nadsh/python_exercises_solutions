# Important things:
# * If you want, handle non-whole years.
#   Use math.floor() or int() to round down non-whole numbers.

def get_salary(years, children):
    """
    This is a comment.
    Calculates salary according to the rules. Years are rounded down to whole number.
    This is a comment.
    """
    salary = 0
    salary += 400 
    salary += 20 * int(years)
    salary += 30 * children
    return salary
    # Alternative: return 400 + (20*years) + (30*children)

years = int(float(input("How many years? (fractions allowed) ")))
children = int(input("How many children? (fractions NOT allowed) "))

print(get_salary(years, children))