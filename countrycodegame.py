country={'IN':["India",'Delhi',1300000000],'US':['America','washington',3200000000],'CA':['Canada','Ottawa',940000],'AU':["Australia",'Canberra',240000000]}
def show_code():
    print('Country codes = ',end=' ')
    for a in country:
        print(a, end =' ')
    print()
def view( ):
    show_code()
    x= input ("enter country code : ")
    if x not in country:
        print("country code doesnt exists .")

    for b,d in country.items():
        if b==x:
            print("country name is : " ,d[0],"\ncountry capital is :",d[1],"\ncountry population is:",d[2])

def addcode():
    x=input("enter country code : ")
    y =input ('enter country name : '),input("enter country capital : " ),input("enter population : ")
    if x in country :
        print('country already exist. ')
    else:
        country[x]=list(y)
        print('new country added .')
        print(country)


def dele():
    show_code()
    x= input("enter country code for delete : ")
    y=country.pop(x,"not found")
    print('deleted country : ',y)



i=0
while i<1:
    entry=input("select an option : \n view :view country name \n add : add a country \n del =delete a country \n exit =exit the program \n")

    if entry == "view":
        view()
    elif entry =='add':
        addcode()
    elif entry =='del':
        dele()
    elif entry =="exit":
        break