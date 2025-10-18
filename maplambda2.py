b = lambda a: True if a in ('a', 'e', 'i', 'o', 'u') else False

name = input('enter your name')
c = filter(b, name)

if len(list(c)) != 0:
    print(list(c))
else:
    print("no vowel in your name")

print(list(c))
print(list(c))
print(list(c))
