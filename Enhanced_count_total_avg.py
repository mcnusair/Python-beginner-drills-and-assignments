# Write a program which repeatedly reads numbers until the user enter "done", print out count, total and average of numbers
count=0
total=0.0
while True:
    sval=input("Enter a number")
    if sval=="done":
        break
    try:
        fval=float(sval)
    except:
        print("Invalid input")
        continue
    print(fval)
    count=count+1
    total=total+fval
    average=total/count
print ("All done!")
print(count, total, average)
