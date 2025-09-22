hrs = input ("Enter hours: ")
rt = input ("Enter rate: ")
try:
    h = float(hrs)
    r = float (rt)
except:
    print ("Error, please enter numeric input")
    quit()
if h<=40:
    p = h*r
    print ("Pay:", p)
else:
    p = 40 * r
    hxtra = h - 40
    pxtra = hxtra * r * 1.5
    ptotal = p + pxtra
    print(ptotal)