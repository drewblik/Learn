a = [1, 3, 5, 7, 9, 11]
c = []
for x in a:
    c.append(x * 2)
print(c)
d = [x * 2 for x in a]
print(d)
e = []
for x in range(1,7):
    e.append(x ** 2)
print(e)
e2 = [x ** 2 for x in range(1,7)] #use for loops to build lists
print(e2)
i = 6
f = []
while i > 0:
    f.append(i **2)
    i -= 1
print(f)
g = [x ** 2 for x in range(6, 0, -1)] #go down in range
print(g)


