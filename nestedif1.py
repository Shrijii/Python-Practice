#
# a= int(input ("enter first no :"))
# b= int(input ("enter second no :"))
# c= int(input ("enter third no :"))
a,b,c = input("enter 3 integers :").split()
a=int (a)
b= int(b)
c=int(c)

if a>b :
    if a>c:
        print(a,"is the highest no")
    else :
        print (c, "is the highest no .")
else:
    if b>c:
        print(b, "is the highest no")
    else :
        print(c, "is the highest no")