a= []
c=[]
print("enter a int ,to stop enter 0")
while True :
    b= int (input())
    if b <= 0 :
        break
    else:
        a.append(b)
print("given list is :", a)
# for x in a:
#     if x%2==0:
#         c.append(x)
# print("inside given list even no.list is given below :")
# print(c)

x=[b for b in a if b%2==0]
print(x)