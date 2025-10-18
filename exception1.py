# import traceback
#
# i=0
# while i<1:
#     try:
#         a = int(input("enter 1st integer : "))
#         b = int(input("enter 2nd integer :"))
#         c = a / b
#         print("Division is :", c)
#         break
#     except :
#         print(traceback.format_exc( ))
#     # except ZeroDivisionError:
#     #     print("Denominator should be non-Zero!")
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"  # Developer-friendly

    def __str__(self):
        return f"{self.name}, {self.age} years old"  # User-friendly

p = Person("Alice", 25)

print(p)   # Calls __str__ → Output: Alice, 25 years old
p         # Console calls __repr__ → Output: Person('Alice', 25)
