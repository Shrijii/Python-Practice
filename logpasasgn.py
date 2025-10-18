def get_fullname():
    i=0
    while i<1:
       x=input ("enter full name : ")
       user = x.split()
       y = x.replace(" ", "")

       if len(user)< 2:
        print("Please enter full name. ")
       elif not y.isalpha():
           print("Please enter name in string .")
       else :
           i+=1
    return x

def get_pass():
    i=0

    while i<1:
        a=input("type your password : ")

        if len(a)<8:
           print("Password must be of 8 and more characters in length with atleast one digit and 1 capital letter .")
        elif not any(x.isupper() for x in a):
            print("Password must be of 8 and more characters in length with atleast one digit and 1 capital letter .")
        elif not any(x.isdigit() for x in a):
            print("Password must be of 8 and more characters in length with atleast one digit and 1 capital letter .")
        else:
            i+=1
    return a

def get_firstname(name):
    x=name.split()
    return x[0]

full_name =get_fullname()
pwd= get_pass()
firstname=get_firstname(full_name)
print("Hello",firstname,"\nThank you for joining us!")


