# Finding the smallest value in a set of numbers

smallest=None
print("Before")
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif smallest>value:
        smallest=value
    print(smallest, value)
print("After", smallest)
quit()