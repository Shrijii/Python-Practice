# def cal_area(radius=1,pi=3.14):
#     area= 2*pi*radius
#     print("Area of circle is", area)
# rad = float(input("enter radius : "))
# cal_area(rad)

def findlargest(*a):
    b=0
    y=1
    for x in a:
        y=y+1
        if len(x)<=len(a[y]):
                continue
        else :
            return len(x),x




print(findlargest("amit","deepak","surya","rajan"))