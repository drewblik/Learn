a = int(input("a = ")) # = because we are assigning a value
b = int(input("b = "))
if a < b:
    print("a is less than b")
    print("a is definitely less than b")
elif a == b: # == because we are evaluating two variables
    print("a is equal to b")
elif a > b + 10:
    print("a is greater than b by more than 10")
else: # a > b
    print("a is NOT less than b")


