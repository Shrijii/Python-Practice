a= input("enter a string: ")
ch=''
for x in a :
    if x.isalnum() or x.isspace():
        ch+=x
ch=ch.split()
print(ch)