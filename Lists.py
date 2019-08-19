#how to declare a list
a = [3, 10, -1]
print(a)
a.append(1)
print(a)
#lists can contain numbers and strings
a.append("hello")
print(a)
#list within a list
a.append([1, 2])
print(a)
a.pop() #deletes last item
print(a)
print(a[4])
a[0] = 100
print(a[0])

#practice
b = ["bananna", "apple", "microsoft"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)