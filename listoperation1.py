num =[]
num2=[]
num3=[num,num2]
copy=[]
n=0
for x in num3:
   n=n+1
   print("enter 5 unique elements for ",n," list: ")
   while len(x)!=5:
       a= int(input("enter element: "))
       if a not in x:
         x.append(a)
       else :
         print("Item already exists.")
         continue
# print("Integer inputted by you are :")
# for x in num:
#     print(x)

# print("enter 5 unique elements for second list: ")
# while len(num2)!=5:
#      a= int(input("enter element: "))
#      if a not in num2:
#          num2.append(a)
#      else :
#          copy.append(a)
#          print("Item already exists.")
#          continue


# print("Integer inputted by you are :")
# for x in num2:
#     print(x)

for x in num:
    if x in num2:
        copy.append(x)
if len(copy)==0:
    print("these lists have no common elements")
else:
    print("these lists have ",len(copy)," common elements")
    print(copy)