# def inspect(x):
#     if len(x)%2==0:
#         return('EVEN')
#     else:
#         return(x[0])
# str=['January','February','March']
# # for y in str:
# #     inspect(y)
# print(list(map(inspect,str) ))
# def a(x):
#     return x*x
# y=[3,4,5,6]
# for t in y:
#     c=a(t)
#     print(c)


#
#
# print (list(map(lambda st : 'Even' if len(st)%2==0 else st[0] ,['january','february','march'])))


b=lambda a: True if a in ('a','e','i','o','u') else False

name=input('enter your name')
c= filter(b,name)

if len(list(c))!=0:
    print(list(c))
else:
    print("no vowel in your name")

print(list(c))
print(list(c))
print(list(c))
