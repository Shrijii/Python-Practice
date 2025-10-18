# str1="bhopal"
# mylist=[ch  for ch in str1]
# print(mylist)
import math
import operator

#
# b= [x**2 for x in range(1,6)]
# print(b)

# a=input('type  a string: ').split(" ")
# b=[]
# for x in a :
#     b.append(x)
# print(b)

# c= [y for y in a]
# print(c)


# a= (input ('type a string :'))
# s=""
# t=" "
# b=[]
# for x in a :
#     if x!=t:
#         s=s+x
#         if a.rindex(x)  == len(a)-1:
#            b.append(s)
#            break
#     else :
#         b.append(s)
#         s=""
# print(b)

# a=[]
# d=0
# b=input("enter 5 integer :").split()
# for x in b:
#     c=int (x)
#     a.append(x)
#     d+=c
# print(a)
# print(d)


# a=input("enter 5 integer : ").split()
# b=[int(x)  for x in a  ]
# print(b)
# print(sum(b))

# def removevowel(str):
#     x=[a for a in str if a not in 'aeiouAEIOU ']
#     print(x)
#
# a = input ("enter a string : ")
# print("original string is : ",a)
# print(removevowel(a))

# def getnumber(str):
#     x=[y for y in str if type(y)is int]
#     return x
# a=["bhopal",25,"$","hello",34,21,"indore",22]
# print (getnumber(a))


# def getlen(z):
#     x=[len(y) for y in z if y not in "theTHE"]
#     return x
# a=input('enter a string : ').split()
# print(getlen(a))

# def getupper(str):
#     x=[a for a in str if 65<=ord(a)<=90 if a not in "AEIOU"]
#     return x
# a=input('enter a string : ')
# print(getupper(a))


def removeminmax(intg):
    x= [a for a in intg if a!=max(intg) or a!=min(intg)]
    return x
a=input ('enter 10 integer :')
print(removeminmax(a))