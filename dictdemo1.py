# s={'virat':480,"rphit":230,"hardik":490,"kedar":700}
# max=0
# p1=''
# for x in s.items():
#     name,score=x
#     if max< score:
#         max=score
#         p1=name
# print ("highest player and its score is :",max,p1)

#
# def sum1(*a):
#     print(sum(a))
# sum1(29,535,51,7393,25643,35,2,4,5,34,3,36,54,134,645,46,346,4)


dict1={"a":1,'b':2,'c':3}
dict2 ={x:"even" if y%2==0 else "odd" for (x,y) in dict1.items() }
print(dict2)