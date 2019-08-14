name = input("Enter name: ")
height = 1.778
weight = 68

bmi = round(weight / (height ** 2)) # ** means to the power of a number
print("bmi: ")
print(bmi)
print(name)
if bmi < 18:
    print("is underweight")
elif bmi > 18 and bmi < 24: # comparison statements are literally "and" "or" "not"
    print("is healthy")
else:
    print("is overweight")
