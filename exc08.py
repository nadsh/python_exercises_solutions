# Important things:
# * Decide on a strategy for getting a boolean input from the user.
#   bool(input()) DOESNT WORK!
def get_salary(years, children, did_attend_every_day_of_work):
    """
    Calculates salary according to the rules. Years are rounded down to whole number.
    """
    salary = 0
    salary += 400 # Minimum
    salary += 20 * int(years)
    salary += 30 * children
    if did_attend_every_day_of_work:
        salary += 100
    return salary
    # Alternative: return 400 + (20*years) + (30*children)

years = int(float(input("How many years? (fractions allowed) ")))
children = int(input("How many children? (fractions NOT allowed) "))
did_attend_str = input("Did attend every day of work? (yes/no) ")

# When checking for "yes", I allow many options for fun.
# When checking for "no", I allow only lower case "no".
if did_attend_str.lower() in ["yes", 'y', 'true', 'positive', 'affirmative']: 
    did_attend = True
elif did_attend_str == "no":
    did_attend = False
else:
    raise Exception(f'Expected a yes/no answer to did_attend, but got {did_attend_str}') 

print(get_salary(years, children, did_attend))