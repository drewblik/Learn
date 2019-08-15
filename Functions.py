#a function is a collection of code
def function1():
    print("ahhh")
    print("baaa")
    print("chaa")
print("outside function")
function1()
# a mapping example
def function2(x):
    return x*2

a = function2(3) #"return value" is 6
print(a)

def function3(x, y):
    return x * y
e = function3(2, 5)
print(e)

def function4(x):
    print(x)
    print("still in this function")
    return 3*x
f = function4(4)
print(f)

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
print(bmi_calculator("Drew",1.7,68))
k = int(input("Enter kilometers: "))
def km_to_miles(km):
    return km / 1.6
print(km_to_miles(k))