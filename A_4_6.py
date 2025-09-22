def computepay(h,r):
    if h <= 40:
        return h*r
    else:
        return (40*r)+((h-40)*1.5*r)
hrs = input ("Enter hours")
rate = input ("Enter rate")
try:
    h=float(hrs)
    r=float(rate)
except:
    print("Error! please enter a numeric value")
p=computepay(h,r)
print("Pay",p)
quit()