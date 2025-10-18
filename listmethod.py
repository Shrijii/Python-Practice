print('enter any 5 random no:')
b=[]
for x in range(0,5):
    a= int(input())
    index=0
    for y in b:
        if y>a:
            break
        index= index+1
    b.insert(index,a)
print('sorted list is:')
print(b)
