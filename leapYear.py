a= int(input("enter a year : "))
if a%4 ==0  :
    if a%400 ==0  :
        print("yes ! it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("it is not a leap year")