a = ["bananna", "apple", "microsoft"]
for element in a:
    print(element)
    print(element)
b = [1, 2, 3]
total = 0
for e in b:
    print(e)
    total = total + e
    print(total)
c = list(range(1, 5)) #creates a range of numbers from 1-5 excluding 5 with range and list function
print(c)
total2 = 0
for i in range(1,7):
    print(i)
    total2 += i
print(total2)
total3 = 0
for i in range(1,8):
    if i % 3 == 0:
        total3 += i
print(total3)

# practice
d = [3, 5]
e = []
for i in d:
    for r in range(1, 100):
        temp = i * r
        if temp < 100:
            e.append(temp)
print(e)
total4 = 0
for element in e:
    total4 += element
print(total4)
total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)