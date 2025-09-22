scr = input ("Please enter score:")
try:
    sc = float (scr)
except ValueError:
    print ("Please enter a numeric value")
    quit()
if 0.0 <= sc <=1.0:
    if sc >= 0.9:
        print ("A")
    elif sc >= 0.8:
        print ("B")
    elif sc >= 0.7:
        print("C")
    elif sc >= 0.6:
        print("D")
    elif sc < 0.6:
        print("F")
else:
    print("Please enter a value between 0.0 and 1.0")
quit()