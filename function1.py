# def absolute(num):
#     if num<0:
#         num= -1*num
#         print (num)
#     else:
#         print(num)
#
# a=int(input("enter an integer : "))
# absolute(a)


# def greet(name):
#     print("hello",name)
#     return"J"print("hello")
# greet('hi')

def cal (a,b):
    c=a+b
    d=a-b
    return c,d
a=int(input('1st no: '))
b=int(input('2nd no: '))
x,y =cal(a,b)
print(x,y)
print(type(x),type(y))
cal(a=14)
print(x,y)