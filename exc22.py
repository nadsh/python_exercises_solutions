# Take care with edge cases. Weird commans at the end, quotation marks, the likes.
# In the example of the question they wanted to have:
#      "positive", 
# with a trailing comma. They also wanted quotation marks.
#
# Exact solution doesn't matter, it's just important to respect the possibilities and make an informed decision.
result = ''
for i in range(5):
    num = float(input("Give "))
    assert num != 0, "Must be positive or negative."
    result += '"Positive", ' if num > 0 else '"Negative", '
print(result)