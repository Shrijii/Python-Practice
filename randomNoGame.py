import random
a= random.randint(1,100)
print ("WELCOME TO THE GAME OF SECRET GUESSING .")
print ("Let's Go")
print("if you want to quit enter 0 or any negative integer : ")
while 1<=a<=100:
   b= input("guess a Secret No. : ")
   b= int(b)
   if 0<b and b<a :
         print('sorry your guess is too small')
   elif  0<b and b> a:
          print ("sorry your guess is too large")
   elif b==a :
        print("Yeah! you guessed it right. ")
        break

   elif b<=0:
         print("Sad you are quitting.")
         print("better luck next time")
         print("Secret no is",a)
         break
   print ("Try again, You are going good")
