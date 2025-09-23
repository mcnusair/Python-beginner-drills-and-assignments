# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    op=line.upper()
    salida=op.rstrip()
    print(salida)